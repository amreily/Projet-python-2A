import csv
import os

def calculate_variations(input_csv, output_csv):
    try:
        # Lire le fichier CSV d'entrée
        with open(input_csv, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)

        # Vérifier que le fichier contient des données
        if len(data) < 2:
            raise ValueError("Le fichier CSV doit contenir au moins un en-tête et une ligne de données.")

        # Extraire l'en-tête et les données
        header = data[0]
        rows = data[1:]

        if header != ["Date", "Close"]:
            raise ValueError("Le fichier CSV doit contenir les colonnes 'Date' et 'Close' dans cet ordre.")

        # Calculer les variations
        variations = [("Date", "Variation (%)")]
        for i in range(1, len(rows)):
            previous_close = float(rows[i-1][1])
            current_close = float(rows[i][1])
            variation = ((current_close - previous_close) / previous_close) * 100
            variations.append((rows[i][0], round(variation, 2)))

        # Écrire les résultats dans un fichier CSV de sortie
        with open(output_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(variations)

        print(f"Les variations ont été calculées et enregistrées dans {output_csv}.")

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Utilisation
input_csv = "cac40_trimestre_filtered.csv"  # Remplacez par le chemin de votre fichier d'entrée
output_csv = "output_variations.csv"  # Chemin pour le fichier de sortie

calculate_variations(input_csv, output_csv)
