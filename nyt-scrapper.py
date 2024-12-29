import requests
import pandas as pd
from datetime import datetime, timedelta
import time
import os

# Configuration
API_KEY = "D26RTqR74kjjaopDptodzz8lKomncUTM"  # clé API NYT
QUERY = "CAC 40"
START_DATE = datetime(2000, 1, 1)  # Début de janvier 2000
END_DATE = datetime(2020, 4, 19)   # Fin de novembre 2024
OUTPUT_FILE = "mentions_cac40.csv"

# URL de l'Article Search API
BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"


# Fonction pour formater les dates au format AAAAMMJJ
def format_date(date):
    return date.strftime("%Y%m%d")


# Fonction pour récupérer les articles depuis l'API NYT
def fetch_articles(query, start_date, end_date, api_key):
    all_articles = []
    page = 0

    print("Recherche des articles en cours...")
    while True:
        # Préparer les paramètres de la requête
        params = {
            'q': query,
            'begin_date': format_date(start_date),
            'end_date': format_date(end_date),
            'api-key': api_key,
            'page': page,
            'sort': 'newest'
        }

        # Envoyer la requête
        response = requests.get(BASE_URL, params=params)
        if response.status_code != 200:
            print(f"Erreur API : {response.status_code}")
            break

        data = response.json()
        docs = data.get('response', {}).get('docs', [])

        if not docs:
            break  # Sortir si plus d'articles

        # Extraire les données nécessaires
        for article in docs:
            all_articles.append({
                'headline': article['headline']['main'],
                'snippet': article.get('snippet', ''),
                'pub_date': article.get('pub_date', ''),
                'web_url': article.get('web_url', '')
            })

        print(f"Page {page + 1} traitée ({len(docs)} articles)")
        page += 1

        if page % 5 == 0:
            print("Pause imposée par l'API...")
            time.sleep(60)

    return all_articles


# Fonction principale
def main():
    global END_DATE
    # Chemin du fichier
    file_name = "mentions_cac40.csv"

    # Tester si le fichier existe
    if os.path.isfile(file_name):
        # Charger le fichier CSV
        df = pd.read_csv("mentions_cac40.csv")

        # Convertir la colonne `pub_date` en format datetime
        df['pub_date'] = pd.to_datetime(df['pub_date'])

        # Trouver la date minimale
        derniere_date = df['pub_date'].min()

        # Convertir en datetime.date pour garder uniquement la date
        if isinstance(derniere_date, pd.Timestamp):
            derniere_date = derniere_date.to_pydatetime().date()

        # Ajouter un jour à la date
        END_DATE = derniere_date + timedelta(days=1)

    articles = fetch_articles(QUERY, START_DATE, END_DATE, API_KEY)

    if not articles:
        print("Aucun article trouvé.")
        return

    # Sauvegarder les résultats dans un fichier CSV
    df = pd.DataFrame(articles)
    df.to_csv(OUTPUT_FILE, mode='a', index=False)
    print(f"{len(articles)} articles sauvegardés dans '{OUTPUT_FILE}'.")


if __name__ == "__main__":
    main()
