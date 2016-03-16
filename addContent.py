import sqlite3 as lite
from datetime import date
import datetime

def ajouterLivre():

    livreTitre = input("Entrez le titre du livre:\n")
    livreAuteur = input("Entrez le nom de l'auteur:\n")
    ISBNLivre = input("Entrez le ISBN:\n")
    datePublicationLivre = input("Entrez la date de publication:\n")

    unLivre = (livreTitre, livreAuteur, ISBNLivre, datePublicationLivre)

    con = lite.connect("TP2.db")

    with con:

        cur = con.cursor()
        cur.execute("INSERT INTO Livres(nomLivre, nomAuteur, ISBN, datePublication) VALUES(?, ?, ?, ?)", unLivre)

    #Faire la condition qui empêche d'ajouter un livre qui existe déjà.

def ajouterMembre():

    nomMembre = input("Entrez le nom:\n")
    telMembre = input("Entrez le numéro de téléphone:\n")

    unMembre = (nomMembre, telMembre)

    con = lite.connect("TP2.db")

    with con:

        cur = con.cursor()
        cur.execute("INSERT INTO Membres VALUES(?, ?)", unMembre)

    #Faire la condition où nomEntré != nomsDansBD.

def ajouterEmprunt():

    ISBNEmprunt = input("Entrez le ISBN du livre emprunté:\n")
    nomMembreEmprunt = input("Entrez le nom du membre qui l'emprunte:\n")
    dateOut = date.today()
    dateDue= dateOut + datetime.timedelta(days=14)

    unEmprunt = (ISBNEmprunt, nomMembreEmprunt, dateOut, dateDue)

    con = lite.connect("TP2.db")

    with con:

        cur = con.cursor()
        cur.execute("INSERT INTO Emprunts(ISBN, nomMembre, dateOut, dateDue) VALUES(?, ?, ?, ?)", unEmprunt)

    #Faire la condition où un abonné ne peut emprunter plus de 3 livres.
    #Faire la condition où on ne peut sortir un livre qui n'existe pas.
    #Faire la condition où on ne peut sortir un livre pour un abonné qui n'existe pas.
    #Faire la condition où on ne peut sortir un livre qui est déjà sorti.

###