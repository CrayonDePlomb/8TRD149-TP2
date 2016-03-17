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

    livreTitre = input("Entrer un titre de livre \n")
    sql = "Select ISBN from Book where title= \"{0}\"".format(livreTitre)


    try:
        cur = db.cursor()
        cur.execute(sql)
        data = cur.fetchall()

        for row in data:
            isbn = row[0]
            print("isbn de l'exemplaire ajouté {0}".format(isbn))
            sql = "INSERT INTO Book_copy(ISBN) VALUES ({0});".format(isbn)
            cur = db.cursor()
            cur.execute(sql)
            print("exemplaire ajouté \n")

        db.commit()
    except:
        db.rollback()

    db.close()


def selectExemplaire():
    db = mysql.connector.connect(user="root", database="tp2DB")
    cur = db.cursor()

    livreTitre = input("Entrer un titre de livre : \n")
    sql = "Select copyNo from Book b ,Book_copy bc where b.ISBN = bc.ISBN and b.title = \"{0}\"".format(livreTitre)
    try:
        cur = db.cursor()
        cur.execute(sql)
        data = cur.fetchall()

        print("Voici liste des exemplaires du livre \"{0}\" : ".format(livreTitre))
        for row in data:
            copyNo = row[0]
            print(" - Numero de copie : {0}\n".format(copyNo))
        db.commit()
    except:
        db.rollback()
    db.close()




def ajouterMembre():

    db = mysql.connector.connect(user="root", database="tp2DB")
    cur = db.cursor()

    nomMembre = input("Entrez le nom:\n")
    adresseMembre = input("Entrer l\'adresse de l'utilisateur\n")
    sql = "INSERT INTO Borrower(borrowerName, borrowerAddress) VALUES (\"{0}\",\"{1}\")".format(nomMembre,adresseMembre)
    try:
        cur.execute(sql)

        db.commit()
    except:
        db.rollback()
    db.close()


def selectLivre():
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
    uneDate = input("Veuillez entrer une date pour vérifier si le livre est disponible(YYYY-MM-DD)\n")

    sql = "SELECT b.title,b.year FROM BookLoan bl,Book_copy bc,Book b where bl.dateOut < \'{0}\' " \
          "AND bl.datedue > \'{0}\' and bl.copyNo = bc.copyNo and bc.ISBN= b.ISBN".format(uneDate)

    try:
        cur = db.cursor()
        cur.execute(sql)
        data = cur.fetchall()

        for row in data:
            title = row[0]
            year = row[1]
            print("Titre : {0} et l\'année: {1}".format(title,year))

        db.commit()
    except:
        db.rollback()
    db.close()

def ajouterEmprunt():
    db = mysql.connector.connect(user="root", database="tp2DB")
    cur = db.cursor()

    nomAbonne = input("Entrer le nom de l\'abonné: \n")
    titreLivre = input("Entrer le titre du livre à emprunter: \n")
    dateInput = input("Entrer la date de sortie de l\'emprunt: \n")
    dateInputConvertie = datetime.datetime.strptime(dateInput, "%Y-%m-%d")
    dateOutputConvertie = dateInputConvertie + datetime.timedelta(days=14)

    sql= "INSERT INTO bookloan VALUES ((SELECT copyNo FROM Book b, book_copy bc WHERE b.ISBN = bc.ISBN AND b.title = " \
         "\"{0}\" ORDER BY bc.copyNo LIMIT 1), \'{1}\', \'{2}\',(SELECT borrowerNo FROM borrower WHERE borrowerName =" \
         " \"{3}\"))".format(titreLivre, dateInputConvertie.strftime("%Y-%m-%d"), dateOutputConvertie.strftime("%Y-%m-%d"), nomAbonne)
    try:
        cur.execute(sql)

        db.commit()
    except:
        db.rollback()
    db.close()


