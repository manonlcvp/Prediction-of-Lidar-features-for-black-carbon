# Prédiction des Paramètres Lidar du Black Carbon avec le Machine Learning

Ce projet vise à prédire les paramètres lidar et physiques du black carbon en utilisant plusieurs méthodes de machine learning (ML). L'objectif principal est d'explorer les relations entre ces paramètres et d'identifier les variables les plus importantes pour la prédiction.

---

## Structure du Projet
Le projet comprend plusieurs notebooks dédiés à des tâches spécifiques :

- [X_Y.ipynb](Notebooks-ML/X_Y.ipynb) : Prédiction des paramètres optiques à partir des paramètres physiques.
- [X_L.ipynb](Notebooks-ML/X_L.ipynb) : Prédiction des paramètres lidar à partir des paramètres physiques.
- [L_X.ipynb](Notebooks-ML/L_X.ipynb) : Prédiction des paramètres physiques à partir des paramètres lidar.
- [L_X_1_2_var.ipynb](Notebooks-ML/L_X _1_2_var.ipynb) : Prédiction des paramètres physiques en utilisant une ou deux variables lidar, pour déterminer les variables les plus influentes.
- [Resultats.ipynb](Notebooks-ML/Resultats.ipynb) : Visualisation des résultats avec des graphes.
- [Fonction_prédiction.ipynb](Notebooks-ML/Fonction_prédiction.ipynb) : Fonction qui prédit les paramètres physiques en prenant en entrée les paramètres Lidar et deux paramètres physiques (fraction of coating et fractal dimension).

### Préparation des données
Les données ont été nettoyées et analysées pour assurer leur qualité et leur exploitabilité avant d'être utilisées dans les modèles. Ce nettoyage a été réalisé dans [création_database.ipynb](data/création_database.ipynb)

---

## Méthodes de Machine Learning
Les algorithmes utilisés pour la prédiction incluent :
- **KRR** (Kernel Ridge Regression)
- **XGB** (Extreme Gradient Boosting)
- **GB** (Gradient Boosting)
- **ANN** (Artificial Neural Networks)

Pour chaque modèle, les performances sont évaluées à l'aide des métriques suivantes :
- **R²** (Coefficient de détermination)
- **MSE** (Mean Squared Error)
- **MAPE** (Mean Absolute Percentage Error)

---

## Résultats et Visualisations
Les résultats sont présentés sous forme de :
- **Graphes des valeurs réelles vs prédictions** : pour visualiser la précision des modèles.
- **Graphes de résidus** : pour évaluer les erreurs de prédiction.
- **Analyse des erreurs de prédiction** : R², MSE, et MAPE sont calculés pour comparer les performances des modèles.

Ces analyses permettent de tester l'importance des différentes variables dans les prédictions et d'optimiser les modèles.

---

## Utilisation
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/manonlcvp/Prediction-of-Lidar-features-for-black-carbon.git
   ```

2. Explorez les notebooks :
   - Commencez par [X_Y.ipynb](Notebooks-ML/X_Y.ipynb), [X_L.ipynb](Notebooks-ML/X_L.ipynb), [L_X.ipynb](Notebooks-ML/L_X.ipynb) ou [L_X_1_2_var.ipynb](Notebooks-ML/L_X _1_2_var.ipynb) pour comprendre les prédictions spécifiques.
   - Consultez [resultats.ipynb](Notebooks-ML/resultats.ipynb) pour visualiser et analyser les résultats.
   - Testez des prédictions avec [Fonction_prédiction.ipynb](Notebooks-ML/Fonction_prédiction.ipynb).

---

## Auteurs

- **Misselis Emiri** - Etudiante INSA Toulouse
- **Catalogna Lise** - Etudiante INSA Toulouse
- **Lacave-Pistaa Manon** - Etudiante INSA Toulouse

---

Ce projet a été réalisé grâce à la contribution de tous les membres mentionnés ci-dessus et de **Ceolato Romain**, encadrant du projet travaillant à l'ONERA. 
