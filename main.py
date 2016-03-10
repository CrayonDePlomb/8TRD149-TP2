import createDatabase #Création de la base de donnée.
import addContent #Fonctions permettant l'ajout de contenu.
import giveContent #Fonctions permettant de récupérer du contenu.

def displayMenu():
    print("Choisissez l'option qui vous convient:\n"
          # 1- Ajoute un livre sans les conditions demandés dans le devoir. Auto-incrémentation de idLivre.
          "1: Ajouter un nouveau livre.\n"
          # 2- Ajoute un nouveau membre sans les conditions demandés dans le devoir.
          "2: Ajouter un nouveau membre.\n"
          # 3- Ajoute un nouvel emprunt sans les conditions dans le devoir. Les dates sont encore en string.
          "3: Effectuer un nouvel emprunt.\n"
          # 4- Sors la liste des livres sans le patron de recherche.
          "4: Sortir la liste des livres. \n"
          "5: Sortir la liste des exemplaires d'un livre.\n"
          "6: Ajouter un nouvel exemplaire d'un livre..\n"
          # 9- Supprime la table au complet et repart à zéro.
          "9: Supprimer la table et recommencer à zéro.\n"
          "0: Sortir du programme.\n")

displayMenu()
choix = input("Entrez votre choix: \n")
if choix == "0":
    print("À la prochaine!")

elif choix == "1":
    addContent.ajouterLivre()
    print("Le nouveau livre a été ajouté.\n")

elif choix == "2":
    addContent.ajouterMembre()
    print("Le nouveau membre a été ajouté.\n")

elif choix == "3":
    addContent.ajouterEmprunt()
    print("L'emprunt a été entré.\n")

elif choix == "4":
    patronRecherche = input("Entrez un mot ou un titre pour rechercher le livre:\n")
    print("Voici la liste des livres:\n")
    giveContent.recupLivres(patronRecherche)

elif choix == "5":
    print("Voici la liste des exemplaires du livre: \n")

elif choix == "6":
    print("Le nouvel exemplaire a été ajouté: \n")

elif choix == "9":
    createDatabase.create()
    print("La base de donnée a été créé.\n")