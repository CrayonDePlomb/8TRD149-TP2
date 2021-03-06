from datetime import date
import datetime
import mysql.connector

user = "root"
password = ""
database = "tp2db"

#AJOUT D'UN LIVRE
def ajouterLivre():
    db = mysql.connector.connect(user=user, password=password, database= database)

    ISBNLivre = input("Entrez le ISBN (8 chiffres et 1er chiffre différent de 0):\n")
    livreTitre = input("Entrez le titre du livre:\n")
    livreYear = input("Entrez l\'année du livre (YYYY):\n")
    livreEdition = input("Entrez l\'édition du livre (Au moins un chiffre):\n")

    sql = "INSERT INTO Book VALUES({0},\"{1}\",{2},{3});".format(ISBNLivre,livreTitre,livreYear,livreEdition)

    try:
        cur = db.cursor()
        cur.execute(sql)
        print("Le nouveau livre a été ajouté.\n")
        db.commit()

    except:
        db.rollback()
        print("\n /!\ L'opération a échoué. /!\ \n")

    db.close()


#AJOUT D'UN EXEMPLAIRE
def ajouterExemplaire():
    db = mysql.connector.connect(user=user, password=password, database= database)

    livreTitre = input("Entrer un titre de livre \n")
    sql = "INSERT INTO Book_copy(ISBN) SELECT ISBN FROM Book WHERE title= \"{0}\"".format(livreTitre)

    try:
        cur = db.cursor()
        cur.execute(sql)

        print("L\'exemplaire a été ajouté\n")
        db.commit()

    except:
        db.rollback()
        print("\n /!\ L'opération a échoué. /!\ \n")

    db.close()


#RECHERCHE DES EXEMPLAIRES D'UN LIVRE
def selectExemplaire():
    db = mysql.connector.connect(user=user, password=password, database= database)

    livreTitre = input("Entrer un titre de livre : \n")
    sql = "SELECT copyNo FROM Book b ,Book_copy bc WHERE b.ISBN = bc.ISBN AND b.title = \"{0}\"".format(livreTitre)
    try:
        cur = db.cursor()
        cur.execute(sql)
        data = cur.fetchall()

        print("Voici liste des exemplaires du livre \"{0}\" : ".format(livreTitre))
        for row in data:
            copyNo = row[0]
            print(" - Numero de copie : {0}\n".format(copyNo))

        print("La recherche d\'exemplaire est terminée \n")
        db.commit()

    except:
        db.rollback()
        print("\n /!\ L'opération a échoué. /!\ \n")

    db.close()


#AJOUT D'UN MEMBRE
def ajouterMembre():

    db = mysql.connector.connect(user=user, password=password, database= database)
    cur = db.cursor()

    nomMembre = input("Entrez le nom:\n")
    adresseMembre = input("Entrer l\'adresse de l'utilisateur\n")
    sql = "INSERT INTO Borrower(borrowerName, borrowerAddress) VALUES (\"{0}\",\"{1}\")".format(nomMembre,adresseMembre)
    try:
        cur.execute(sql)

        print("L\'abonné a été ajouté\n")
        db.commit()

    except:
        db.rollback()
        print("\n /!\ L'opération a échoué. /!\ \n")

    db.close()

#RECHERCHE D'UN LIVRE SELON PATRON
def selectLivre():
    db = mysql.connector.connect(user=user, password=password, database= database)

    livreTitre = input("Entrer un titre de livre \n")
    sql = "SELECT title FROM Book WHERE title LIKE \"%{0}%\"".format(livreTitre)
    try:
        cur = db.cursor()
        cur.execute(sql)
        data = cur.fetchall()

        print("Voici la liste des titres trouver : \n")
        for row in data:
            name = row[0]
            print("- {0} \n".format(name))

        print("Le patron de recherche est terminé \n")
        db.commit()

    except:
        db.rollback()
        print("\n /!\ L'opération a échoué. /!\ \n")

    db.close()


#RECHERCHE DISPONIBILITE D'UN LIVRE SELON UNE DATE
def rechercheSelonUnedate():
    db = mysql.connector.connect(user=user, password=password, database= database)
    uneDate = input("Veuillez entrer une date pour vérifier si le livre est disponible(YYYY-MM-DD)\n")

    sql = "SELECT b.title,b.year FROM BookLoan bl,Book_copy bc,Book b WHERE bl.dateOut <= \'{0}\' " \
          "AND bl.datedue > \'{0}\' AND bl.copyNo = bc.copyNo AND bc.ISBN= b.ISBN".format(uneDate)

    try:
        cur = db.cursor()
        cur.execute(sql)
        data = cur.fetchall()

        for row in data:
            title = row[0]
            year = row[1]
            print("Titre : {0} et l\'année: {1}".format(title,year))

        print("Le patron de recherche est terminé \n")
        db.commit()

    except:
        db.rollback()
        print("\n /!\ L'opération a échoué. /!\ \n")

    db.close()


#AJOUT D'UN EMPRUNT
def ajouterEmprunt():
    db = mysql.connector.connect(user=user, password=password, database= database)

    nomAbonne = input("Entrer le nom de l\'abonné: \n")
    titreLivre = input("Entrer le titre du livre à emprunter: \n")
    dateInput = input("Entrer la date de sortie de l\'emprunt: (YYYY-MM-DD) \n")
    dateInputConvertie = datetime.datetime.strptime(dateInput, "%Y-%m-%d")
    dateOutputConvertie = dateInputConvertie + datetime.timedelta(days=14)

    sql= "INSERT INTO bookloan VALUES ((SELECT copyNo FROM Book b, book_copy bc WHERE b.ISBN = bc.ISBN AND b.title = " \
         "\"{0}\" AND bc.available=TRUE ORDER BY bc.copyNo LIMIT 1), \'{1}\', \'{2}\',(SELECT borrowerNo FROM borrower WHERE borrowerName =" \
         " \"{3}\"))".format(titreLivre, dateInputConvertie.strftime("%Y-%m-%d"), dateOutputConvertie.strftime("%Y-%m-%d"), nomAbonne)
    try:
        cur = db.cursor()
        cur.execute(sql)

        db.commit()
        print("Le nouvel emprunt a été ajouté. \n")

    except:
        db.rollback()
        print("\n /!\ L'opération a échoué. /!\ \n")

    db.close()


