import pandas as pd

# Lecture du fichier CSV existant
file_path = "chomage_final.csv"
df = pd.read_csv(file_path)

# Filtrage pour conserver uniquement les données à partir de l'année 2000
df = df[df['date'] >= '2000-T1']

# Transformation des trimestres (T1, T2, ...) en équivalents numériques (3, 6, ...)
df['date'] = df['date'].str.replace(r'-T1', '-03', regex=True)
df['date'] = df['date'].str.replace(r'-T2', '-06', regex=True)
df['date'] = df['date'].str.replace(r'-T3', '-09', regex=True)
df['date'] = df['date'].str.replace(r'-T4', '-12', regex=True)

# Sauvegarde du fichier modifié
output_path = "0_chomage_final.csv"
df.to_csv(output_path, index=False)

output_path
