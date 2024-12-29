import pandas as pd

# Load the CSV file
file_path = 'ipc.csv'
data = pd.read_csv(file_path, skiprows=3)  # Skip the metadata rows

# Keep only the relevant columns
final_data = data[['Période', 'indice']]
final_data.columns = ['Date', 'Indice']

# Save the cleaned data to a new CSV file
output_path = 'ipc_final.csv'
final_data.to_csv(output_path, index=False)

output_path
