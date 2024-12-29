import requests
import pandas as pd
from io import BytesIO
import zipfile

# Fonction permettant de récupérer des fichiers depuis leur adresse URL.
def url_df(url, excel_name=None, sheet_name=None, save_as_csv=False, csv_name="output.csv"):
    try:
        response = requests.get(url)  # Télécharge le fichier
        response.raise_for_status()
        
        # Vérifie si c'est un zip
        content_type = response.headers.get('Content-Type', '').lower()
        if 'zip' in content_type or url.endswith('.zip'):
            print("Le fichier téléchargé est un fichier zip.")
            zip_content = BytesIO(response.content)
            with zipfile.ZipFile(zip_content) as zip:  # Corrigé ici

                if excel_name is None:
                    excel_name = next((f for f in zip.namelist() if f.endswith('.xlsx')), None)
                    if excel_name is None:
                        raise FileNotFoundError("Aucun fichier Excel trouvé dans le zip.")
                    print(f"Fichier Excel non spécifié, utilisation de : {excel_name}.")
                
                if excel_name not in zip.namelist():
                    raise FileNotFoundError(f"Le fichier '{excel_name}' est introuvable dans le zip.")
                
                with zip.open(excel_name) as excel:
                    excel_data = pd.ExcelFile(BytesIO(excel.read())) 
        
        # Si ce n'est pas un zip, on suppose que c'est un fichier Excel
        elif 'excel' in content_type or url.endswith('.xlsx'):
            print("Le fichier téléchargé est un fichier Excel.")
            excel_data = pd.ExcelFile(BytesIO(response.content))
        
        else:
            raise ValueError("Le fichier téléchargé n'est ni un fichier Excel, ni un fichier zip.")
        
        if sheet_name is None:
            sheet_name = excel_data.sheet_names[0]
            print(f"Feuille non spécifiée, chargement de : {sheet_name}")
        
        # Création d'un dataframe
        df = excel_data.parse(sheet_name)
        print(f"Feuille '{sheet_name}' chargée.")
        
        # Sauvegarde en CSV si demandé
        if save_as_csv:
            df.to_csv(csv_name, index=False, encoding='utf-8-sig')
            print(f"Fichier sauvegardé au format CSV sous le nom : {csv_name}")
        
        return df
    
    except Exception as e:
        print(f"Erreur : {e}")
        return None
