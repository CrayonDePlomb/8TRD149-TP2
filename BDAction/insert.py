from datetime import date
import datetime
import MySQLdb



def ajouterLivre():
    db = MySQLdb.connect("localhost","root","","tp2DB")
    cur = db.cursor()

    ISBNLivre = input("Entrez le ISBN:\n")
    livreTitre = input("Entrez le titre du livre:\n")
    livreYear = input("Entrez l\'année du livre :\n")
    livreEdition = input("Entrez l\'edition du livre\n")

    sql = "INSERT INTO Book VALUES({0},\"{1}\",{2},{3});".format(ISBNLivre,livreTitre,livreYear,livreEdition)

    try:
        cur.execute(sql)
        db.commit()

    except:
        db.rollback()

    db.close()

def ajouterExemplaire():
    db = MySQLdb.connect("localhost","root","","tp2DB")
    cur = db.cursor()

    ISBNLivre = input("Entrez le ISBN:\n")

    sql = "INSERT INTO Book_copy(ISBN) VALUES ({0});".format(ISBNLivre)

    try:
        cur.execute(sql)
        db.commit()

    except:
        db.rollback()

    db.close()


def selectLivre():
    db = MySQLdb.connect("localhost","root","","tp2DB")
    cur = db.cursor()
    if(db.close()):
        db = MySQLdb.connect("localhost","root","","tp2DB")
    livreTitre = input("Entrer un titre de livre")

    sql = "Select title from Book where title = {0}".format(livreTitre)
    try:
        cur = db.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        nbData = cur.rowcount

        for data in range(0,nbData):
            print("Voici la liste trouver pour un titre : {0} \n".format(data))

        db.commit()
    except:
        db.rollback()
    db.close()




def ajouterMembre():

    db = MySQLdb.connect("localhost","root","","tp2DB")
    cur = db.cursor()

    if(db.close()):
        db = MySQLdb.connect("localhost","root","","tp2DB")
    idMembre = input("Entrer un id : \n")
    nomMembre = input("Entrez le nom:\n")
    adresseMembre = input("Entrer l\'adresse de l'utilisateur\n")

    sql = "INSERT INTO Borrower VALUES ({0},{1},{2})".format(idMembre,nomMembre,adresseMembre)

    try:
        cur = db.cursor()
        cur.execute(sql)
    except:
        db.rollback()
    db.close()


def patronDeRecherche():
    db = MySQLdb.connect("localhost","root","","tp2DB")
    cur = db.cursor()

    livreTitre = input("Entrer un titre de livre \n")
    sql = "Select title from Book where title LIKE \"%{0}%\"".format(livreTitre)
    try:
        cur = db.cursor()
        cur.execute(sql)
        data = cur.fetchall()

        for row in data:
            name = row[0]
            print("Voici la liste des titres trouver : {0} \n".format(name))

        db.commit()
    except:
        db.rollback()
    db.close()

def rechercheSelonUnedate():
    db = MySQLdb.connect("localhost","root","","tp2DB")
    cur = db.cursor()
    if(db.close()):
        db = MySQLdb.connect("localhost","root","","tp2DB")
    uneDate = input("Veuillez entrer une date pour vérifier si le livre est disponible")

    sql = "SELECT * FROM BookLoan,Book_copy,Book where dateOut > {0} AND datedue < {1}".format(uneDate)

    try:
        cur = db.cursor()
        cur.execute(sql)
        date = cur.fetchall()
        nbData = cur.rowcount

        for data in range(0,nbData):
            print("Titre : {0} et l\'année: {1}".format(data["Book.title"],data["Book.year"]))
    except:
        db.rollback()
    db.close()

