import pandas as pd

# Charger le fichier CSV
file_path = 'confiance_final_final.csv'
data = pd.read_csv(file_path)

# Garder les lignes correspondant à des mois multiples de 3 (3,6,9,12)
data['Month'] = pd.to_datetime(data['Date'], format='%Y-%m')
data['Month_Num'] = data['Month'].dt.month
data['Year'] = data['Month'].dt.year
filtered_data = data[(data['Year'] >= 2000) & (data['Month_Num'].isin([3, 6, 9, 12]))]

# Sauvegarder le résultat dans un nouveau fichier
output_path = '0_confiance_final.csv'
filtered_data[['Date', 'Value']].to_csv(output_path, index=False)

output_path
