import pandas as pd

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv("mentions_cac40.csv")

# Supprimer les doublons en gardant seulement le premier article par date
df_unique = df.drop_duplicates(subset=['pub_date'], keep='first')

# Sauvegarder le résultat dans un nouveau fichier CSV
df_unique.to_csv("articles_uniques_par_date.csv", index=False)

print("Traitement terminé. Le fichier 'articles_uniques_par_date.csv' contient les articles sans doublons par date.")
