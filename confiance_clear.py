import pandas as pd

# Lire le fichier CSV original
df = pd.read_csv('confiance.csv')

# Identifiez les colonnes fixes (sans 'Label') et les colonnes de périodes
fixed_columns = ['idBank', 'Last update', 'Period']  # Exclure 'Label'
period_columns = [col for col in df.columns if col not in fixed_columns + ['Label']]

# Transformez les colonnes de périodes en lignes
df_melted = df.melt(id_vars=fixed_columns, value_vars=period_columns,
                    var_name='Date', value_name='Value')

# Exportez le fichier transformé en CSV
df_melted.to_csv('confiance_clear.csv', index=False)

print("Fichier transformé en tableur CSV classique sans la colonne 'Label'.")
