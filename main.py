import createDatabase #Création de la base de donnée.
import addContent #Fonctions permettant l'ajout de contenu.
import giveContent #Fonctions permettant de récupérer du contenu.

import mysql.connector

from BDAction import insert

def displayMenu():
    print("Choisissez l'option qui vous convient:\n"
          # 1- Ajoute un livre sans les conditions demandés dans le devoir. Auto-incrémentation de idLivre.
          "1: Ajouter un nouveau livre.\n"
          # 2- Ajoute un nouveau membre sans les conditions demandés dans le devoir.
          "2: Sortir la liste des livres selon un patron de recherche sur le titre.\n"
          # 3- Ajoute un nouvel emprunt sans les conditions dans le devoir. Les dates sont encore en string.
          "3: Ajout d\'un nouvel exemplaire.\n"
          # 4- Sors la liste des livres sans le patron de recherche.
          "4: Sortir la liste des exemplaires d'un livre avec le titre exact.\n"
          "5: Ajouter un nouvel abonné.\n"
          "6: Ajouter un nouvel exemplaire d'un livre..\n"
          "7: Ajouter un nouvel emprunt d'un livre..\n"
          # 9- Supprime la table au complet et repart à zéro.
          "9: Supprimer la table et recommencer à zéro.\n"
          "0: Sortir du programme.\n")

displayMenu()
choix = input("Entrez votre choix: \n")
if choix == "0":
    print("À la prochaine!")

elif choix == "1":
    insert.ajouterLivre()

elif choix == "2":
    insert.selectLivre()

elif choix == "3":
    insert.ajouterExemplaire()

elif choix == "4":
     insert.selectExemplaire()

elif choix == "5":
    insert.ajouterMembre()

elif choix == "6":
    insert.rechercheSelonUnedate()

elif choix == "7":
    insert.ajouterEmprunt()

elif choix == "9":
    createDatabase.create()
    print("La base de donnée a été créé.\n")
