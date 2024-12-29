# Projet python 2A

*Par Carla LUCAS, Amrei LYTIN, Alban NELIAS, 2024.*

Dans ce projet python pour la data science, nous souhaitions modéliser les valeurs du CAC40 à partir de variables macroéconomiques (PIB, inflation, chômage, confiance) et des taux directeurs de la Banque Centrale Européenne. 

Ce projet s'est décliné en plusieurs étapes : 
- l'importation des données depuis Internet
- le nettoyage des données ainsi que leur mise en un format permettant la modélisation
- la recherche du modèle pertinent pour expliquer les valeurs du CAC40

# Table des matières
1. [Définitions](#definitions)
2. [Objectif du projet](#objectif-du-projet)
3. [Sources des données](#sources)

## 1. Définitions <a name="definitions">

**CAC 40 :** 

Le CAC 40 est le principal indice boursier de la Bourse de Paris. C'est un indice flottant pondéré en fonction de la capitalisation boursière qui reflète la performance des 40 actions les plus importantes et les plus activement négociées cotées sur Euronext Paris.

(Source : https://fr.wikipedia.org/wiki/CAC_40.)

**Croissance du PIB :** 

La croissance est l'évolution du produit intérieur brut (PIB) sans tenir compte de la variation des prix. 

(Source : https://www.insee.fr/fr/statistiques/fichier/2549709/Insee-En-Bref-PIB-vFR-Interactif.pdf)

**Inflation :**

L'inflation est la perte du pouvoir d'achat de la monnaie qui se traduit par une augmentation générale et durable des prix.

(Source : https://www.insee.fr/fr/metadonnees/definition/c1473#:~:text=L'inflation%20est%20la%20perte,%2C%20entreprises%2C%20etc.)

**Chômage :**

Le taux de chômage est le pourcentage de chômeurs dans la population active (actifs occupés + chômeurs).
On peut calculer un taux de chômage par âge en mettant en rapport les chômeurs d'une classe d'âge avec les actifs de cette classe d'âge. De la même manière se calculent des taux de chômage par sexe, par PCS, par région, par nationalité, par niveau de diplôme...

(Source : https://www.insee.fr/fr/metadonnees/definition/c1687)

**Confiance :** 

L'indicateur synthétique de confiance des ménages résume leur opinion sur la situation économique : plus sa valeur est élevée, plus le jugement des ménages sur la situation économique est favorable.

(Source : https://www.insee.fr/fr/statistiques/7928049#:~:text=(apr%C3%A8s%20arrondi).-,Pour%20en%20savoir%20plus,la%20situation%20%C3%A9conomique%20est%20favorable.)

**Taux directeurs :** 

Les taux directeurs sont les taux d'intérêt au jour le jour fixés par la banque centrale d'un pays ou d'une union monétaire, et qui permettent à celle-ci de réguler l'activité économique.

(Source : https://fr.wikipedia.org/wiki/Taux_directeur)

## 2. Objectif du projet <a name="objectifs">

Nous cherchons à expliquer les valeurs du CAC40 en fonction des variables susnommées. 

## 3. Sources des données <a name="sources">

Nous avons utilisé les sources suivantes : 

- Insee
- API Yahoo Finance
- New York Times
- Banque Centrale Européenne

Les données sont récupérées soit par une fonction qui, via une URL, crée un DataFrame, soit par une API.
