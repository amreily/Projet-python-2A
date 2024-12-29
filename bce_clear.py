import pandas as pd

# Charger le fichier CSV
file_path = 'bce_interest_rates.csv'
data = pd.read_csv(file_path)

# Convertir la colonne 'date' en format datetime
data['date'] = pd.to_datetime(data['date'])

# Filtrer les données à partir de l'année 2000
data_filtered = data[data['date'].dt.year >= 2000]

# Garder uniquement les lignes correspondant aux mois de mars, juin, septembre et décembre (3, 6, 9, 12)
data_final = data_filtered[data_filtered['date'].dt.month.isin([3, 6, 9, 12])]

# Garder uniquement les 1ers de ces mois
data_final = data_final[data_final['date'].dt.day == 1]

# Nom du fichier de sortie
output_file_path = 'filtered_bce_interest_rates.csv'

# Sauvegarder les données filtrées dans un nouveau fichier CSV
data_final.to_csv(output_file_path, index=False)

# Indiquer à l'utilisateur que le fichier a été créé
f"Le fichier filtré a été sauvegardé sous le nom : {output_file_path}"
