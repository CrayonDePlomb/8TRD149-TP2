from datetime import date
import datetime
import mysql.connector



def ajouterLivre():
    db = mysql.connector.connect(user="root", database="tp2DB")
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
    db = mysql.connector.connect(user="root", database="tp2DB")
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
    db = mysql.connector.connect(user="root", database="tp2DB")
    cur = db.cursor()
    if(db.close()):
        db = mysql.connector.connect(user="root", database="tp2DB")
    livreTitre = input("Entrer un titre de livre")

    sql = "Select title,copyNo from Book,Book_copy where Book.ISBN = Book_copy.ISBN and title = {0}".format(livreTitre)
    try:
        cur = db.cursor()
        cur.execute(sql)
        data = cur.fetchall()

        for row in data:
            title = row[0]
            copyNo = row[1]
            print("Title : {0} et Le numero de Copy : {1}".format(title,copyNo))
        db.commit()
    except:
        db.rollback()
    db.close()




def ajouterMembre():

    db = mysql.connector.connect(user="root", database="tp2DB")
    cur = db.cursor()
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
    db = mysql.connector.connect(user="root", database="tp2DB")
    cur = db.cursor()

    livreTitre = input("Entrer un titre de livre \n")
    sql = "Select title from Book where title LIKE \"%{0}%\"".format(livreTitre)
    try:
        cur = db.cursor()
        cur.execute(sql)
        data = cur.fetchall()

        print("Voici la liste des titres trouver : \n")
        for row in data:
            name = row[0]
            print("- {0} \n".format(name))

        db.commit()
    except:
        db.rollback()
    db.close()

def rechercheSelonUnedate():
    db = mysql.connector.connect(user="root", database="tp2DB")
    cur = db.cursor()
    if(db.close()):
        db = mysql.connector.connect(user="root", database="tp2DB")
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
