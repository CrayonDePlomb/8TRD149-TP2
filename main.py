import createDatabase #Création de la base de donnée.

import mysql.connector

from BDAction import insert

def displayMenu():
    print("Choisissez l'option qui vous convient:\n"
          "1: Ajouter un nouveau livre.\n"
          "2: Sortir la liste des livres selon un patron de recherche sur le titre.\n"
          "3: Ajout d\'un nouvel exemplaire de livre en fournissant ses détails.\n"
          "4: Sortir la liste des exemplaires d'un livre avec le titre exact.\n"
          "5: Ajouter un nouvel abonné.\n"
          "6: Sortir la liste des exemplaires de livres empruntés selon une date de recherche.\n"
          "7: Ajouter un nouvel emprunt d'un livre.\n"
          "8: Supprimer la table et recommencer à zéro.\n"
          "0: Sortir du programme.\n")

choix = " "
while choix != 0:
    displayMenu()
    choix = input("Entrez votre choix: \n")

    if choix == "0":
        print("////////////////////////////////////////////////////////////\n")
        choix = 0
        print("À la prochaine!")

    elif choix == "1":
        print("////////////////////////////////////////////////////////////\n")
        insert.ajouterLivre()
        print("////////////////////////////////////////////////////////////\n")

    elif choix == "2":
        print("////////////////////////////////////////////////////////////\n")
        insert.selectLivre()
        print("////////////////////////////////////////////////////////////\n")

    elif choix == "3":
        print("////////////////////////////////////////////////////////////\n")
        insert.ajouterExemplaire()
        print("////////////////////////////////////////////////////////////\n")

    elif choix == "4":
         print("////////////////////////////////////////////////////////////\n")
         insert.selectExemplaire()
         print("////////////////////////////////////////////////////////////\n")

    elif choix == "5":
        print("////////////////////////////////////////////////////////////\n")
        insert.ajouterMembre()
        print("////////////////////////////////////////////////////////////\n")

    elif choix == "6":
        print("////////////////////////////////////////////////////////////\n")
        insert.rechercheSelonUnedate()
        print("////////////////////////////////////////////////////////////\n")

    elif choix == "7":
        print("////////////////////////////////////////////////////////////\n")
        insert.ajouterEmprunt()
        print("////////////////////////////////////////////////////////////\n")

    elif choix == "8":
        print("////////////////////////////////////////////////////////////\n")
        createDatabase.create()
        print("La base de donnée a été créé.\n")
        print("////////////////////////////////////////////////////////////\n")
