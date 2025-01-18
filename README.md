# Prédiction des Paramètres Lidar du Black Carbon avec le Machine Learning

Ce projet vise à prédire les paramètres lidar et physiques du black carbon en utilisant plusieurs méthodes de machine learning (ML). L'objectif principal est d'explorer les relations entre ces paramètres et d'identifier les variables les plus importantes pour la prédiction.

---

## Structure du Projet
Le projet comprend plusieurs notebooks dédiés à des tâches spécifiques :

- [X_Y.ipynb](Notebooks-ML/X_Y.ipynb) : Prédiction des paramètres optiques à partir des paramètres physiques.
- [X_L.ipynb](Notebooks-ML/X_L.ipynb) : Prédiction des paramètres lidar à partir des paramètres physiques.
- [L_X.ipynb](Notebooks-ML/L_X.ipynb) : Prédiction des paramètres physiques à partir des paramètres lidar. Ce notebook inclut également une étude détaillée de la prédiction des paramètres physiques en utilisant une ou deux variables lidar, pour déterminer les variables les plus influentes.
- [resultats.ipynb](Notebooks-ML/resultats.ipynb) : Visualisation des résultats avec des graphes.

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
- **Analyse des erreurs de prédiction** : R², MSE, et MAPE sont calculés pour comparer les performances des modèles.

Ces analyses permettent de tester l'importance des différentes variables dans les prédictions et d'optimiser les modèles.

---

## Utilisation
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/manonlcvp/Prediction-of-Lidar-features-for-black-carbon.git
   cd Prediction-of-Lidar-features-for-black-carbon
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. Explorez les notebooks :
   - Commencez par [X_Y.ipynb](Notebooks-ML/X_Y.ipynb), [X_L.ipynb](Notebooks-ML/X_L.ipynb), ou [L_X.ipynb](Notebooks-ML/L_X.ipynb) pour comprendre les prédictions spécifiques.
   - Consultez [resultats.ipynb](Notebooks-ML/resultats.ipynb) pour visualiser et analyser les résultats.