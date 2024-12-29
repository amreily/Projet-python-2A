import pandas as pd

input_path = 'articles_uniques_par_date.csv'  # Chemin du fichier d'entrée
output_path = 'nbr_mentions.csv'  # Chemin du fichier de sortie

# Lire les données depuis le fichier CSV
df = pd.read_csv(input_path)

# Vérifier si la colonne 'pub_date' existe
if 'pub_date' not in df.columns:
    raise ValueError("La colonne 'pub_date' n'existe pas dans le fichier.")

# Convertir la colonne 'Date' en format datetime
try:
    df['Date'] = pd.to_datetime(df['pub_date'], errors='coerce')
except Exception as e:
    raise ValueError(f"Erreur lors de la conversion des dates : {e}")

# Identifier et retirer les valeurs non valides
invalid_dates = df[df['Date'].isna()]
if not invalid_dates.empty:
    print(f"Dates invalides détectées :\n{invalid_dates}")
    # Supprimer les lignes avec des dates non valides
    df = df.dropna(subset=['Date'])

# Définir les périodes : 1 janvier, 1 mars, 1 juin, 1 septembre
def assign_period(date):
    if date.month in [1, 2]:
        return f"{date.year}-01-01"
    elif date.month in [3, 4, 5]:
        return f"{date.year}-03-01"
    elif date.month in [6, 7, 8]:
        return f"{date.year}-06-01"
    elif date.month in [9, 10, 11]:
        return f"{date.year}-09-01"
    else:  # Décembre
        return f"{date.year}-12-01"

# Ajouter une colonne pour la période
df['Period'] = df['Date'].apply(assign_period)

# Grouper par période et compter les articles
article_counts = df.groupby('Period').size().reset_index(name='Article Count')

# Sauvegarder le résultat dans un nouveau fichier CSV
article_counts.to_csv(output_path, index=False)

print(f"Les résultats ont été sauvegardés dans : {output_path}")
