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

def benchmark(tailles:list[int], erase:bool, output_excel:str, diagram_name:str, tri:list[bool]):
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
        resultats["Taille"].append(taille)
        # Génération de la liste aléatoire
        tab = random.sample(range(taille * random.randint(5,15)), taille)

        # Tri à Bulle
        if tri[0]:
            tab_copy = tab.copy()
            start_time = time.perf_counter()
            tri_a_bulle(tab_copy)
            bulle_time = time.perf_counter() - start_time
            resultats["Bulle (s)"].append(bulle_time)
        else:
            resultats["Bulle (s)"].append("-")
            bulle_time = "-"
            

        # Tri Rapide
        if tri[1]:
            tab_copy = tab.copy()
            start_time = time.perf_counter()
            tri_rapide(tab_copy)
            rapide_time = time.perf_counter() - start_time
            resultats["Rapide (s)"].append(rapide_time)
        else:
            resultats["Rapide (s)"].append("-")
            rapide_time = "-"

        # Tri par Fusion
        if tri[2]:
            tab_copy = tab.copy()
            start_time = time.perf_counter()
            tri_fusion(tab_copy)
            fusion_time = time.perf_counter() - start_time
            resultats["Fusion (s)"].append(fusion_time)
        else:
            resultats["Fusion (s)"].append("-")
            fusion_time = "-"

        # Tri par Insertion
        if tri[3]:
            tab_copy = tab.copy()
            start_time = time.perf_counter()
            tri_insertion(tab_copy)
            insertion_time = time.perf_counter() - start_time
            resultats["Insertion (s)"].append(insertion_time)
        else:
            resultats["Insertion (s)"].append("-")
            insertion_time = "-"

        # Tri par Casier
        if tri[4]:
            tab_copy = tab.copy()
            start_time = time.perf_counter()
            tri_casier(tab_copy)
            casier_time = time.perf_counter() - start_time
            resultats["Casier (s)"].append(casier_time)
        else:
            resultats["Casier (s)"].append("-")
            casier_time = "-"        

        print(f"[+] Taille {taille} : Bulle {bulle_time}s, Rapide {rapide_time}s, Fusion {fusion_time}s, Insertion {insertion_time}s, Casier {casier_time}s")
        
    # Sauvegarde des résultats dans un fichier Excel
    df_resultats = pd.DataFrame(resultats)
    save_excel(df_resultats, output_excel, erase)

    # Création du diagramme
    plt.figure(figsize=(10, 6))

    if tri[0]: plt.plot(df_resultats["Taille"], df_resultats["Bulle (s)"], label="Tri à Bulle", marker='o')
    if tri[1]: plt.plot(df_resultats["Taille"], df_resultats["Rapide (s)"], label="Tri Rapide", marker='o')
    if tri[2]: plt.plot(df_resultats["Taille"], df_resultats["Fusion (s)"], label="Tri par Fusion", marker='o')
    if tri[3]: plt.plot(df_resultats["Taille"], df_resultats["Insertion (s)"], label="Tri par Insertion", marker='o')
    if tri[4]: plt.plot(df_resultats["Taille"], df_resultats["Casier (s)"], label="Tri par Casier", marker='o')
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
    tri = [False] * 5
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
    
    choix = input("Tester  le tri a bulle ? (O/N ou Y/N) : ").strip().lower()
    if choix in ["n", "non", "n", "no"]:
        tri[0] = False
    else:
        tri[0] = True
    choix = input("Tester  le tri Rapide ? (O/N ou Y/N) : ").strip().lower()
    if choix in ["n", "non", "n", "no"]:
        tri[1] = False
    else:
        tri[1] = True
    choix = input("Tester  le tri fusion ? (O/N ou Y/N) : ").strip().lower()
    if choix in ["n", "non", "n", "no"]:
        tri[2] = False
    else:
        tri[2] = True
    choix = input("Tester  le tri a insertion ? (O/N ou Y/N) : ").strip().lower()
    if choix in ["n", "non", "n", "no"]:
        tri[3] = False
    else:
        tri[3] = True
    choix = input("Tester  le tri casier  ? (O/N ou Y/N) : ").strip().lower()
    if choix in ["n", "non", "n", "no"]:
        tri[4] = False
    else:
        tri[4] = True
    
    benchmark(tailles, erase, excel_name, diagram_name,tri)