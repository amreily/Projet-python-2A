import requests
import pandas as pd

def fetch_ecb_interest_rates():
    # Liste des identifiants de séries pour les taux directeurs
    series_ids = {
        "Main Refinancing Operations (MRO)": "FM.B.U2.EUR.4F.MM.MRO1.RATE",
        "Deposit Facility Rate (DFR)": "FM.B.U2.EUR.4F.MM.DFR.RATE",
        "Marginal Lending Facility (MLF)": "FM.B.U2.EUR.4F.MM.MLF.RATE",
    }

    base_url = "https://data-api.ecb.europa.eu/service/data/"

    headers = {
        "Accept": "application/vnd.sdmx.data+json;version=1.0.0-wd",
    }

    all_rates = []

    for rate_name, series_id in series_ids.items():
        url = f"{base_url}{series_id}"

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Erreur lors de la requête pour {rate_name}: {response.status_code}")
            print(f"Réponse : {response.text}")
            continue

        try:
            data = response.json()
            series = data.get('dataSets', [])[0].get('series', {})
            observations = series.get('0:0:0:0:0', {}).get('observations', {})
            time_periods = data.get('structure', {}).get('dimensions', {}).get('observation', [])[0].get('values', [])

            for index, obs in observations.items():
                date = time_periods[int(index)]['id']
                value = obs[0]
                all_rates.append({"Rate Type": rate_name, "Date": date, "Value": value})
        except Exception as e:
            print(f"Erreur lors de l'analyse des données pour {rate_name} : {e}")

    if all_rates:
        df = pd.DataFrame(all_rates)
        csv_file = "ecb_interest_rates.csv"
        df.to_csv(csv_file, index=False)
        print(f"Données sauvegardées dans {csv_file}")
    else:
        print("Aucune donnée n'a été récupérée.")

# Appel de la fonction
fetch_ecb_interest_rates()
