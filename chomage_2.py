import pandas as pd

# Charger le fichier transposé
file_path = "chomage_transpose.csv"
data = pd.read_csv(file_path, header=None)

# Supposons que la première ligne contient les en-têtes après la transposition
data.columns = data.iloc[0]
data = data[1:]

# Garder uniquement les colonnes "Sexe et âge" et "Ensemble"
filtered_data = data[["Sexe et âge", "Ensemble "]]

# Sauvegarder dans un nouveau fichier CSV
output_path = "chomage_final.csv"
filtered_data.to_csv(output_path, index=False)

print(f"Le fichier filtré a été sauvegardé sous le nom {output_path}.")
