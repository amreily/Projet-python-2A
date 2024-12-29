import pandas as pd

# Nom du fichier source et du fichier de sortie
input_file = "confiance_clear.csv"
output_file = "0_confiance_final.csv"

# Lire le fichier CSV
try:
    data = pd.read_csv(input_file)
    
    # Extraire les colonnes "Date" et "Value"
    filtered_data = data[["Date", "Value"]]

    # Sauvegarder les données filtrées dans un nouveau fichier CSV
    filtered_data.to_csv(output_file, index=False)

    print(f"Les colonnes 'Date' et 'Value' ont été extraites avec succès dans le fichier {output_file}.")
except FileNotFoundError:
    print(f"Le fichier {input_file} est introuvable.")
except KeyError as e:
    print(f"Erreur: {e}. Assurez-vous que les colonnes 'Date' et 'Value' existent dans le fichier source.")
