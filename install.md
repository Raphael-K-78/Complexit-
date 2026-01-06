# Installation du projet

Ce projet utilise **Python**, un **environnement virtuel (venv)** et des **dépendances listées dans `requirements.txt`**.

---

## Prérequis

Avant de commencer, assure-toi d’avoir installé :

- **Python 3.9 ou plus récent**
  - **Vérifier** :
    ```bash
    python --version
    ```
    ou
    ```bash
    python3 --version
    ```
  - Installer :
    
- **Git**
  - **Vérifier** :
    ```bash
    git --version
    ```
  - **Installer** :

---

## Récupération du projet

Cloner le dépôt GitHub :

```bash
git clone https://github.com/Raphael-K-78/Complexit-.git
cd Complexit-
```
## Création de l’environnement virtuel

créer le `venv` :
```bash
python3 -m venv venv
source venv/bin/activate
```
Lorsque l’environnement est activé, le terminal affiche généralement :
```bash
(venv)
```
## Installation des dépendances
Installer les bibliothèques nécessaires :
```bash
pip install -r requirements.txt
```
## Lancer le Projet
- **Benchmark tri** :
    ```bash
    python3 Benchmark_tri.py
    ```
- **Benchmark Recherche** :
    ```bash
    python3 Benchmark_recherche.py
    ```