import pandas as pd

# Charger le fichier CSV
file_path = "chomage.csv"
data = pd.read_csv(file_path, header=None)

# Transposer les données
transposed_data = data.T

# Sauvegarder le fichier transposé
output_path = "chomage_transpose.csv"
transposed_data.to_csv(output_path, index=False, header=False)

print(f"Le fichier transposé a été sauvegardé sous le nom {output_path}.")
