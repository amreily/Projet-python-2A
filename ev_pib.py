import pandas as pd

# Chargement du fichier CSV en sautant les deux premières lignes
data = pd.read_csv('ev_pib.csv', skiprows=3)

# Vérification des noms des colonnes
print(data.columns)

# Conservation des colonnes pertinentes
data_filtered = data[["Trimestre", "Produit intérieur brut (PIB)"]]

# Enregistrement dans un nouveau fichier CSV
data_filtered.to_csv('pib_final.csv', index=False)

print("Le fichier 'pib_final.csv' a été créé avec succès.")
