import pandas as pd

# Essayer de charger le fichier réel pour le traiter (remplacement du contenu fictif)
ipc_file_path = 'ipc_final.csv'

# Charger le fichier CSV
ipc_data = pd.read_csv(ipc_file_path)

# Ajouter une colonne 'Month' pour faciliter le filtrage
ipc_data['Month'] = pd.to_datetime(ipc_data['Date'], format='%Y-%m')
ipc_data['Year'] = ipc_data['Month'].dt.year
ipc_data['Month_Num'] = ipc_data['Month'].dt.month

# Filtrer pour les années >= 2000 et les mois multiples de 3
filtered_ipc_data = ipc_data[(ipc_data['Year'] >= 2000) & (ipc_data['Month_Num'].isin([3, 6, 9, 12]))]

# Sauvegarder le résultat dans un nouveau fichier
ipc_output_path = '0_ipc_final.csv'
filtered_ipc_data[['Date', 'Indice']].to_csv(ipc_output_path, index=False)

ipc_output_path
