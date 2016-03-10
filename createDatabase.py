#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as lite

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


    con = lite.connect('TP2.db')

    with con:

        cur = con.cursor()

        cur.execute("DROP TABLE IF EXISTS Membres")
        cur.execute("CREATE TABLE Membres "
                    "(nomMembre TEXT UNIQUE NOT NULL, "
                    "numTelephone TEXT NOT NULL,"
                    "PRIMARY KEY (nomMembre))")

        cur.executemany("INSERT INTO Membres VALUES(?, ?)", membres)

        cur.execute("DROP TABLE IF EXISTS Emprunts")
        cur.execute("CREATE TABLE Emprunts "
                    "(ISBN TEXT UNIQUE NOT NULL, "
                    "nomMembre TEXT NOT NULL, "
                    "dateOut DATE NOT NULL, "
                    "dateDue DATE NOT NULL, "
                    "disponible BOOLEAN DEFAULT 0,"
                    "PRIMARY KEY (ISBN),"
                    "FOREIGN KEY (nomMembre) REFERENCES Membres(nomMembre))")

        cur.executemany("INSERT INTO Emprunts(ISBN, nomMembre, dateOut, dateDue) VALUES(?, ?, ?, ?)", emprunts)

        cur.execute("DROP TABLE IF EXISTS Livres")
        cur.execute("CREATE TABLE Livres "
                    "(idLivre INTEGER PRIMARY KEY, "
                    "nomLivre TEXT NOT NULL, "
                    "nomAuteur TEXT NOT NULL, "
                    "ISBN TEXT NOT NULL, "
                    "datePublication DATE NOT NULL,"
                    "FOREIGN KEY (ISBN) REFERENCES Emprunts(ISBN))")

        cur.executemany("INSERT INTO Livres(nomLivre, nomAuteur, ISBN, datePublication) VALUES(?, ?, ?, ?)", livres)
