import pandas as pd

#
# Charger le fichier CSV ecb_bce.csv
file_path = 'ebc_bce.csv'
data = pd.read_csv(file_path)

# Convertir la colonne "DATE" en datetime
data['DATE'] = pd.to_datetime(data['DATE'])

# Filtrer les données à partir de l'an 2000
data = data[data['DATE'] >= '2000-01-01']

# Créer un DataFrame avec toutes les dates entre 2000 et aujourd'hui
all_dates = pd.date_range(start='2000-01-01', end=pd.Timestamp.now().normalize())

# Fusionner les données pour inclure toutes les dates et remplir les valeurs manquantes par la dernière valeur connue
data = data.set_index('DATE').reindex(all_dates).rename_axis('DATE').reset_index()
data['Main refinancing operations - fixed rate tenders (fixed rate) (date of changes) - Level (FM.B.U2.EUR.4F.KR.MRR_FR.LEV)'] = data['Main refinancing operations - fixed rate tenders (fixed rate) (date of changes) - Level (FM.B.U2.EUR.4F.KR.MRR_FR.LEV)'].fillna(method='ffill')

# Enregistrer les données remplies dans un nouveau fichier CSV
output_path = 'bce_filled.csv'
data.to_csv(output_path, index=False)

output_path
