import pandas as pd
# Charger le fichier bce_final.csv
file_path_final = 'bce_final.csv'
data = pd.read_csv(file_path_final)

# Garder uniquement les colonnes DATE et la dernière colonne, et renommer cette dernière en "rate"
data = data[['DATE', 'Main refinancing operations - fixed rate tenders (fixed rate) (date of changes) - Level (FM.B.U2.EUR.4F.KR.MRR_FR.LEV)']]
data = data.rename(columns={'Main refinancing operations - fixed rate tenders (fixed rate) (date of changes) - Level (FM.B.U2.EUR.4F.KR.MRR_FR.LEV)': 'rate'})

# Enregistrer dans un nouveau fichier CSV
output_final_final_path = 'bce_final_final.csv'
data.to_csv(output_final_final_path, index=False)

output_final_final_path