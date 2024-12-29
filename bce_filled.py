import pandas as pd

# Charger le fichier bce_filled.csv
file_path_filled = 'bce_filled.csv'
data = pd.read_csv(file_path_filled)

# Convertir la colonne "DATE" en datetime
data['DATE'] = pd.to_datetime(data['DATE'])

# Filtrer pour ne conserver que les dates à partir de l'an 2000
data = data[data['DATE'] >= '2000-01-01']

# Conserver uniquement les dates qui sont les premiers des mois multiples de 3 (mars, juin, septembre, décembre)
data = data[data['DATE'].dt.month.isin([3, 6, 9, 12])]
data = data[data['DATE'].dt.day == 1]

# Enregistrer dans un nouveau fichier CSV
output_final_path = 'bce_final.csv'
data.to_csv(output_final_path, index=False)

output_final_path
