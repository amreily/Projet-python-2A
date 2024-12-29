import pandas as pd

# Charger les fichiers CSV
sortie = pd.read_csv("sortie.csv")
nbr_mentions = pd.read_csv("nbr_mentions.csv")

# Assurez-vous que les colonnes de date sont au format datetime
sortie['Date'] = pd.to_datetime(sortie['Date'], errors='coerce')
nbr_mentions['Date'] = pd.to_datetime(nbr_mentions['Date'], errors='coerce')

# Effectuer la jointure sur la colonne 'date'
resultat = pd.merge(sortie[['Date', 'Close']], nbr_mentions[['Date', 'Article Count']], on='Date', how='inner')

# Sauvegarder le fichier résultant si nécessaire
resultat.to_csv("jointure_resultat.csv", index=False)

print("La jointure a été réalisée avec succès. Le fichier est sauvegardé sous le nom 'jointure_resultat.csv'.")
