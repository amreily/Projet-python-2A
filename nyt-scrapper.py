import requests
import pandas as pd
from datetime import datetime

# Configuration
API_KEY = "D26RTqR74kjjaopDptodzz8lKomncUTM"  # clé API NYT
QUERY = "CAC 40"
START_DATE = datetime(2000, 1, 1)  # Début de janvier 2000
END_DATE = datetime(2024, 12, 1)   # Fin de novembre 2024
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

        if page >= 10:  # Limite de pages imposée par l'API NYT (10 pages max)
            break

    return all_articles


# Fonction principale
def main():
    articles = fetch_articles(QUERY, START_DATE, END_DATE, API_KEY)

    if not articles:
        print("Aucun article trouvé.")
        return

    # Sauvegarder les résultats dans un fichier CSV
    df = pd.DataFrame(articles)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"{len(articles)} articles sauvegardés dans '{OUTPUT_FILE}'.")


if __name__ == "__main__":
    main()
