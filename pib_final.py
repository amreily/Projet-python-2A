import pandas as pd

# Chargement du fichier 'pib_final.csv'
data = pd.read_csv('pib_final.csv')

# Suppression de la première ligne de données
data = data.iloc[1:]

# Transformation des trimestres en mois
def transform_trimester_to_month(trimestre):
    year, quarter = trimestre.split('-')
    month = {
        'T1': '03',
        'T2': '06',
        'T3': '09',
        'T4': '12'
    }.get(quarter, '01')  # Par défaut, janvier
    return f"{year}-{month}"

data['Trimestre'] = data['Trimestre'].apply(transform_trimester_to_month)

# Suppression des lignes avant l'année 2000
data = data[data['Trimestre'] >= '2000-01']

# Enregistrement du fichier nettoyé
data.to_csv('pib_cleaned.csv', index=False)

print("Le fichier 'pib_cleaned.csv' a été créé avec succès.")
