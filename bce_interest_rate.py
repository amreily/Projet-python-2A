import pandas as pd

# Charger le fichier CSV
file_path = 'bce_interest_rates.csv'
data = pd.read_csv(file_path)

# Convertir la colonne 'date' en format datetime
data['date'] = pd.to_datetime(data['date'])

# Trier les données par date
data = data.sort_values(by='date')

# Générer une gamme complète des dates nécessaires entre la première et la dernière date disponible
date_range = pd.date_range(start=data['date'].min(), end=data['date'].max(), freq='D')
complete_data = pd.DataFrame(date_range, columns=['date'])

# Fusionner les données pour inclure toutes les dates
complete_data = pd.merge(complete_data, data, on='date', how='left')

# Remplir les valeurs manquantes par la valeur précédente
complete_data = complete_data.fillna(method='ffill')

# Filtrer les données à partir de l'année 2000
complete_data_filtered = complete_data[complete_data['date'].dt.year >= 2000]

# Garder uniquement les lignes correspondant aux mois de mars, juin, septembre et décembre (3, 6, 9, 12)
complete_data_filtered = complete_data_filtered[complete_data_filtered['date'].dt.month.isin([3, 6, 9, 12])]

# Garder uniquement les 1ers de ces mois
complete_data_filtered = complete_data_filtered[complete_data_filtered['date'].dt.day == 1]

# Nom du fichier de sortie
output_file_path = 'filtered_bce_interest_rates.csv'

# Sauvegarder les données filtrées dans un nouveau fichier CSV
complete_data_filtered.to_csv(output_file_path, index=False)

# Indiquer à l'utilisateur que le fichier a été créé
f"Le fichier filtré a été sauvegardé sous le nom : {output_file_path}"
