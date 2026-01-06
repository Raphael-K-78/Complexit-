import random
import time
import pandas as pd
import matplotlib.pyplot as plt

from recherche.recherche_naive import recherche_naive
from recherche.recherche_dichotomique import recherche_dichotomique
from save_excel import save_excel

def benchmark(tailles, erase, output_excel, diagram_name):
    # Dictionnaire pour stocker les résultats
    resultats = {
        "Taille": [],
        "Naive (s)": [],
        "Dichotomique (s)": []
    }
    # Boucle sur les tailles spécifiées
    for taille in tailles:
        taille = int(taille)
        # Génération de la liste triée et de la cible
        tab = sorted(random.sample(range(taille * random.randint(5,15)), taille))
        cible = random.choice(tab)

        # Recherche Naive
        start_time = time.perf_counter()
        recherche_naive(tab, cible)
        naive_time = time.perf_counter() - start_time

        # Recherche Dichotomique
        start_time = time.perf_counter()
        recherche_dichotomique(tab, cible)
        dichotomique_time = time.perf_counter() - start_time

        resultats["Taille"].append(taille)
        resultats["Naive (s)"].append(naive_time)
        resultats["Dichotomique (s)"].append(dichotomique_time)

        print(f"[+] Taille {taille} : Naive {naive_time:.6f}s, Dichotomique {dichotomique_time:.6f}s")
        
    # Sauvegarde des résultats dans un fichier Excel
    df_resultats = pd.DataFrame(resultats)
    save_excel(df_resultats, output_excel, erase)

    # Création du diagramme
    plt.figure(figsize=(10, 6))
    plt.plot(df_resultats["Taille"], df_resultats["Naive (s)"], label="Recherche Naive", marker='o')
    plt.plot(df_resultats["Taille"], df_resultats["Dichotomique (s)"], label="Recherche Dichotomique", marker='o')
    plt.xlabel("Taille de la liste")
    plt.ylabel("Temps (secondes)")
    plt.title("Benchmark des Algorithmes de Recherche")
    plt.legend()
    plt.grid(True)
    plt.savefig(diagram_name)
    try:
        plt.show()
    except:
        pass
    print(f"\n[+] Diagramme sauvegardé sous {diagram_name}")

if __name__ == "__main__":
    print("Saisir les tailles des listes à tester.")
    print("Appuyer sur Entrée sans rien écrire pour terminer.\n")

    tailles = []
    continuer = True

    while continuer:
        taille = input("Taille de la liste : ")

        if taille == "":
            continuer = False
        else:
            tailles.append(taille)
    
    if len(tailles) == 0:
        print("[-] Il faut au moins une taille de liste pour effectuer les tests.")
        print("[-] Fin du programme.")
        quit()

    excel_name = input("Nom du fichier Excel (ex: resultats.xlsx) : ")
    if excel_name == "":
        excel_name = "resultats.xlsx"
    elif not excel_name.endswith(".xlsx"):
        excel_name += ".xlsx"

    choix = input("Souhaitez-vous écraser le fichier excel (O/N ou Y/N) : ").strip().lower()

    if choix in ["n", "non", "n", "no"]:
        erase = False
    else:
        erase = True
    
    diagram_name = input("Nom du fichier du diagramme (ex: graphique.png) : ")
    if diagram_name == "":
        diagram_name = "graphique.png" 
    elif not (diagram_name.endswith(".png") or diagram_name.endswith(".jpg") or diagram_name.endswith(".jpeg")):
        diagram_name += ".png"

    benchmark(tailles, erase, excel_name, diagram_name)