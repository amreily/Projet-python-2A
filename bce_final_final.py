import pandas as pd

# Nom du fichier source et du fichier de sortie
input_file = "bce_final_final.csv"
output_file = "0_bce_final.csv"

# Lire le fichier CSV
try:
    data = pd.read_csv(input_file)

    # Transformer la colonne "date" pour ne conserver que l'année et le mois
    data['DATE'] = pd.to_datetime(data['DATE']).dt.strftime('%Y-%m')

    # Sauvegarder les données modifiées dans un nouveau fichier CSV
    data.to_csv(output_file, index=False)

    print(f"Les dates ont été formatées et les données enregistrées dans le fichier {output_file}.")
except FileNotFoundError:
    print(f"Le fichier {input_file} est introuvable.")
except KeyError as e:
    print(f"Erreur: {e}. Assurez-vous que les colonnes 'date' et 'rate' existent dans le fichier source.")
