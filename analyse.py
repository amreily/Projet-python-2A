import numpy as np
import pandas as pd

#Calcule la moyenne, l'écart-type, et la variance d'une variable et affiche un tableau avec ces valeurs.

def afficher_statistiques(variable):
    # Calculs statistiques
    moyenne = np.mean(variable)
    ecart_type = np.std(variable, ddof=1)  # ddof=1 pour un échantillon
    variance = np.var(variable, ddof=1)

    # Création d'un tableau avec Pandas
    statistiques = {
        'Statistique': ['Moyenne', 'Écart-type', 'Variance'],
        'Valeur': [moyenne, ecart_type, variance]
    }
    df = pd.DataFrame(statistiques)

    # Affichage du tableau
    print("\nTableau des statistiques :\n")
    print(df)
