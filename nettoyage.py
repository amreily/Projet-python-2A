import pandas as pd

#Filtre un DataFrame pour commencer à partir de la ligne correspondant à une valeur spécifique de trimestre.
def filter_dataframe_by_trimestre(df, trimestre_value):
    # Trouver l'index de la valeur dans la colonne 'trimestre'
    index_value = df[df['trimestre'] == trimestre_value].index
    
    # Vérifier si l'index existe
    if len(index_value) == 0:
        raise ValueError(f"La valeur '{trimestre_value}' n'a pas été trouvée dans la colonne 'trimestre'.")
    
    # Extraire l'index (on prend le premier en cas de doublons)
    index_value = index_value[0]
    
    # Filtrer le DataFrame
    filtered_df = df.iloc[index_value:].reset_index(drop=True)
    
    return filtered_df


# Localise et supprime les lignes contenant des valeurs manquantes (NaN)
def handle_missing_values(df):
    while True:
        # Localiser les lignes contenant des NaN
        missing_rows = df[df.isna().any(axis=1)]
        
        # Si des NaN sont trouvés, les afficher
        if not missing_rows.empty:
            print("Lignes contenant des NaN :")
            print(missing_rows)
        else:
            break  # Si aucune ligne ne contient de NaN, on arrête

        # Supprimer les lignes contenant des NaN
        df = df.dropna()
        df = df.reset_index(drop=True)  # Réinitialiser les index après suppression

        # Vérifier s'il reste des NaN
        nan_count = df.isna().sum().sum()
        print(f"Nombre total de NaN restant : {nan_count}")
        
        if nan_count == 0:
            print("Toutes les valeurs manquantes ont été supprimées.")
            break
    
    return df


# Convertir un DataFrame avec des données journalières en données trimestrielles (moyenne par trimestre).
def convert_to_quarterly(df, date_column, value_columns):
  # Convertir la colonne date en format datetime
    df[date_column] = pd.to_datetime(df[date_column])

    # Mettre la colonne date comme index
    df.set_index(date_column, inplace=True)

    # Resampler les données en moyennes trimestrielles
    df_quarterly = df[value_columns].resample("Q").mean()  # "Q" = fréquence trimestrielle

    # Réinitialiser l'index pour que la date redevienne une colonne
    df_quarterly = df_quarterly.reset_index()

    # Renommer la colonne de date en "trimestre"
    df_quarterly.rename(columns={date_column: 'trimestre'}, inplace=True)

    return df_quarterly

# Transformation de l'écriture des éléments de la colonne trimestre pour que toutes les colonnes soient du même format
def format_trimestre(trimestre):
     # Extraire l'année et le trimestre
     annee = trimestre.year
     mois = trimestre.month
     # Calculer le trimestre en fonction du mois
     if mois in [3]:
         trimestre = "T1"
     elif mois in [6]:
         trimestre = "T2"
     elif mois in [9]:
         trimestre = "T3"
     else:
         trimestre = "T4"
     # Retourner le format "T1.2000"
     return f"{trimestre}.{annee}"
# Appliquer la fonction à chaque date pour créer la nouvelle colonne : confiance['trimestre'] = confiance['trimestre'].apply(format_trimestre)