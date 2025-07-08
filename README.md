## Informations importantes

### Format des fichiers

Les résultats des simulations sont sauvegardés dans des fichiers au **format HDF5**.  
Il est donc essentiel de vérifier que les **packages nécessaires** à la lecture et à l’écriture de ce type de fichier sont bien **installés** sur votre machine.

Il est **vivement recommandé** d’utiliser un environnement **Anaconda**, dans lequel les dépendances nécessaires sont facilement gérables.

---

### Nom du fichier de simulation

Avant chaque simulation, il est indispensable de définir le nom du fichier HDF5 dans lequel seront enregistrés les résultats :  
```python
fichier = "nom_du_fichier.h5"
```

---

### Stabilité des simulations

La **stabilité numérique** des simulations est suivie via l’étude des **résidus**.  
Ces résidus sont calculés comme la **norme infinie** de l’erreur de troncature, **normalisée** par leur valeur initiale.

- Pour une simulation stable, les résidus doivent être constants ou décroissants.
- Si les résidus dépassent un certain **seuil critique** (fixé automatiquement à **10**), la simulation est considérée comme **instable**.



## Description du solveur

Ce solveur résout l’équation de la chaleur 1D à l’aide de la méthode des différences finies.  
Plusieurs schémas spatiaux sont disponibles :
  - Schéma à 3 points : `"Schema3Points"`
  - Schéma à 5 points : `"Schema5Points"`
  - Schéma compact à 3 points : `"SchemaCompact3Points"`

Plusieurs schémas temporels sont également proposés :
  - Schéma d’Euler explicite : `"EulerExplicite"`
  - Schéma d’Euler implicite : `"EulerImplicite"`
  - Schéma de Crank-Nicolson : `"CrankNicolson"`
  - Schéma de Runge-Kutta d'ordre 2 : `"RK2"`
  - Schéma de Runge-Kutta d'ordre 4 : `"RK4"`

## Paramètres physiques

Il est possible de configurer plusieurs paramètres physiques :
  - Longueur du domaine : `L`
  - Nombre de mailles : `N`
  - Pas de temps : `dt`
  - Matériaux disponibles :
    * `"cuivre"`
    * `"aluminium"`
    * `"acier"`
    * `"titane"`
    * `"silicium"`
    * `"verre_pyrex"`

## Conditions aux limites disponibles

  - `["adiabatique"]`  
  - `["conduction", 10]` → conduction avec une température source de 10°C  
  - `["convection", 10, 20]` → convection avec un coefficient de 10 et un milieu extérieur à 20°C

> **Remarque :**  
> Si **les deux conditions aux limites** sont de type **conduction**, une **solution analytique** est automatiquement calculée, ce qui permet de comparer l’exactitude des différents schémas numériques.

## Profil de température initial

  - `["uniforme", 30]` → température constante à 30°C  
  - `["lineaire", 30, 60]` → gradient linéaire de 30°C à 60°C  
  - `["marche", 30, 60, 0.5]` → fonction de Heaviside à x = 0.5  
  - `["porte", 30, 60, 0.5, 0.6]` → température de 60°C entre x = 0.5 et x = 0.6, sinon 30°C

## Paramètres de contrôle de la simulation

  - Temps de départ de la simulation : `debut`  
  - Écriture des résultats : `ecriture`  
  - Intervalle entre deux écritures : `interval`
