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
        choix = 0
        print("À la prochaine!")

    elif choix == "1":
        insert.ajouterLivre()

    elif choix == "2":
        insert.selectLivre()
        print("Le patron de recherche est terminé \n")

    elif choix == "3":
        insert.ajouterExemplaire()
        print("L\'opération a été effectué.\n")

    elif choix == "4":
         insert.selectExemplaire()
         print("La recherche d\'exemplaire est terminée \n")

    elif choix == "5":
        insert.ajouterMembre()

    elif choix == "6":
        insert.rechercheSelonUnedate()
        print("La recherche d\'exemplaire est terminée \n")

    elif choix == "7":
        insert.ajouterEmprunt()

    elif choix == "8":
        createDatabase.create()
        print("La base de donnée a été créé.\n")
