import random
import time
import pandas as pd
import matplotlib.pyplot as plt

from tri.tri_bulle import tri_a_bulle
from tri.tri_rapide import tri_rapide
from tri.tri_fusion import tri_fusion
from tri.tri_insertion import tri_insertion
from tri.tri_casier import tri_casier
from save_excel import save_excel

def benchmark(tailles, erase, output_excel, diagram_name):
    # Dictionnaire pour stocker les résultats
    resultats = {
        "Taille": [],
        "Bulle (s)": [],
        "Rapide (s)": [],
        "Fusion (s)": [],
        "Insertion (s)": [],
        "Casier (s)": []
    }
    # Boucle sur les tailles spécifiées
    for taille in tailles:
        taille = int(taille)
        # Génération de la liste aléatoire
        tab = random.sample(range(taille * random.randint(5,15)), taille)

        # Tri à Bulle
        tab_copy = tab.copy()
        start_time = time.perf_counter()
        tri_a_bulle(tab_copy)
        bulle_time = time.perf_counter() - start_time

        # Tri Rapide
        tab_copy = tab.copy()
        start_time = time.perf_counter()
        tri_rapide(tab_copy)
        rapide_time = time.perf_counter() - start_time

        # Tri par Fusion
        tab_copy = tab.copy()
        start_time = time.perf_counter()
        tri_fusion(tab_copy)
        fusion_time = time.perf_counter() - start_time

        # Tri par Insertion
        tab_copy = tab.copy()
        start_time = time.perf_counter()
        tri_insertion(tab_copy)
        insertion_time = time.perf_counter() - start_time

        # Tri par Casier
        tab_copy = tab.copy()
        start_time = time.perf_counter()
        tri_casier(tab_copy)
        casier_time = time.perf_counter() - start_time

        resultats["Taille"].append(taille)
        resultats["Bulle (s)"].append(bulle_time)
        resultats["Rapide (s)"].append(rapide_time)
        resultats["Fusion (s)"].append(fusion_time)
        resultats["Insertion (s)"].append(insertion_time)
        resultats["Casier (s)"].append(casier_time)

        print(f"[+] Taille {taille} : Bulle {bulle_time:.6f}s, Rapide {rapide_time:.6f}s, Fusion {fusion_time:.6f}s, Insertion {insertion_time:.6f}s, Casier {casier_time:.6f}s")
        
    # Sauvegarde des résultats dans un fichier Excel
    df_resultats = pd.DataFrame(resultats)
    save_excel(df_resultats, output_excel, erase)

    # Création du diagramme
    plt.figure(figsize=(10, 6))
    plt.plot(df_resultats["Taille"], df_resultats["Bulle (s)"], label="Tri à Bulle", marker='o')
    plt.plot(df_resultats["Taille"], df_resultats["Rapide (s)"], label="Tri Rapide", marker='o')
    plt.plot(df_resultats["Taille"], df_resultats["Fusion (s)"], label="Tri par Fusion", marker='o')
    plt.plot(df_resultats["Taille"], df_resultats["Insertion (s)"], label="Tri par Insertion", marker='o')
    plt.plot(df_resultats["Taille"], df_resultats["Casier (s)"], label="Tri par Casier", marker='o')
    plt.xlabel("Taille de la liste")
    plt.ylabel("Temps (secondes)")
    plt.title("Benchmark des Algorithmes de Tri")
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