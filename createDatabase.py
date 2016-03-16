#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb


def create():
    livres = (
        ('Harry Potter à l\'UQAC', 'Daelhi Nadeau-Otis', '1111', "2011-08-30"),
        ('Harry Potter à l\'UQAC', 'Daelhi Nadeau-Otis', '1112', "2011-08-30"),
        ('Chad, mon incroyable vie', 'Chad Coup-Fabiano', '1121', "2013-11-30"),
        ('James le chien', 'Gillian Chaville', '1131', "2014-12-30"),
        ('Le bon loup', 'Daelhi Nadeau-Otis', '1141', "2000-11-30"),
        ('Titre de livre absent', 'Gillian Chaville ', '1151', "2003-11-30"),
        ('Je suis gentil', 'Marilou St-Gelais', '1161', "1999-06-30")
    )

    emprunts = (
        ('1111', 'Bob Le Bricoleur', '2016-03-09', '2016-03-23'),
        ('1121', 'Joey Jeremiah', '2016-03-01', '2016-03-05'),
        ('1161', 'Donald Trump', '2016-03-08', '2016-03-23'),
    )

    membres = (
        ('Bob Le Bricoleur', '4185347965'),
        ('Joey Jeremiah', '4183439696'),
        ('Donald Trump', '4184353877'),
        ('Leonardo Dicaprio', '4185436452'),
    )


    db = MySQLdb.connect("localhost","root","","tp2DB")

    cur = db.cursor()

    cur.execute("DROP TABLE IF EXISTS Book")
    cur.execute("CREATE TABLE Book "
                "(ISBN INT PRIMARY KEY NOT NULL, "
                "title VARCHAR(255) NOT NULL,"
                "year INT(4),"
                "edition INT(2))")

    cur.executemany("INSERT INTO Membres VALUES(?, ?)", membres)

    cur.execute("DROP TABLE IF EXISTS Book_copy")
    cur.execute("CREATE TABLE Book_copy "
                "(copyNo INT(4) PRIMARY KEY NOT NULL, "
                "ISBN INT, "
                "available BOOLEAN,"
                "FOREIGN KEY (ISBN) REFERENCES Book(ISBN))")

    cur.executemany("INSERT INTO Emprunts(ISBN, nomMembre, dateOut, dateDue) VALUES(?, ?, ?, ?)", emprunts)

    cur.execute("DROP TABLE IF EXISTS Borrower")
    cur.execute("CREATE TABLE Borrower "
                "(borrowerNO INT PRIMARY KEY NOT NULL, "
                "borrowerName VARCHAR(255) NOT NULL, "
                "borrowerAddress VARCHAR(255))")

    cur.executemany("INSERT INTO Livres(nomLivre, nomAuteur, ISBN, datePublication) VALUES(?, ?, ?, ?)", livres)

    cur.execute("DROP TABLE IF EXISTS BookLoan")
    cur.execute("CREATE TABLE BookLoan "
                "(copyNo INT(4) NOT NULL, "
                "dateOut DATE PRIMARY KEY, "
                "dateDue DATE,"
                "borrowerNo INT(4),"
                "FOREIGN KEY (borrowerNo) REFERENCES Borrower(borrowerNO))")

    cur.executemany("INSERT INTO Livres(nomLivre, nomAuteur, ISBN, datePublication) VALUES(?, ?, ?, ?)", livres)
