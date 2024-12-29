import pandas as pd

# Chemin vers le fichier CSV original
input_file = 'cac40_trimestre.csv'

# Charger le fichier CSV en sautant les lignes inutiles
column_names = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']
df = pd.read_csv(input_file, skiprows=[0, 1, 2], names=column_names)
# Filtrer les colonnes nécessaires
df_filtered = df[['Date', 'Close']]

# Sauvegarder le nouveau fichier CSV
output_file = 'cac40_trimestre_filtered.csv'
df_filtered.to_csv(output_file, index=False)

print(f"Les données formatées ont été sauvegardées dans '{output_file}'.")
