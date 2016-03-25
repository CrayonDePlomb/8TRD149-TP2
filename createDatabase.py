#!/usr/bin/python
# -*- coding: utf-8 -*-
import mysql.connector

user = "root"
password = "root678"
database = "tp2DB"

def create():


    db = mysql.connector.connect(user=user, password=password, database= database)

    cur = db.cursor()



    cur.execute("SET FOREIGN_KEY_CHECKS=0") # Il ne regarde plus les foreign_key

    cur.execute("DROP TABLE IF EXISTS Book Cascade")
    cur.execute("CREATE TABLE Book "
                "(ISBN INT PRIMARY KEY NOT NULL, "
                "title VARCHAR(255) NOT NULL,"
                "year INT(4),"
                "edition INT(2))")

    cur.execute("LOAD DATA LOCAL INFILE 'Data/Book.csv'"
                    "INTO TABLE Book "
                    "FIELDS TERMINATED BY ','"
                    "ENCLOSED BY '\"'"
                    "LINES TERMINATED BY '\n'"
                    "(ISBN, title, edition, year)")
    db.commit()

    print("Book est crée et remplir\n")

    cur.execute("DROP TABLE IF EXISTS Borrower CASCADE ")
    cur.execute("CREATE TABLE Borrower "
                "(borrowerNo INT(4) NOT NULL AUTO_INCREMENT, "
                "borrowerName VARCHAR(255) NOT NULL, "
                "borrowerAddress VARCHAR(255),"
                "PRIMARY KEY (borrowerNo))")


    cur.execute("LOAD DATA LOCAL INFILE 'Data/Borrower.csv'"
                "INTO TABLE Borrower "
                "FIELDS TERMINATED BY ','"
                "ENCLOSED BY '\"'"
                "LINES TERMINATED BY '\n'"
                "(borrowerNO, borrowerName, BorrowerAddress)")
    db.commit()


    print("Borrower est crée et remplir\n")


    cur.execute("DROP TABLE IF EXISTS BookLoan CASCADE ")
    cur.execute("CREATE TABLE BookLoan "
                "(copyNo INT(4) NOT NULL , "
                "dateOut DATE , "
                "dateDue DATE,"
                "borrowerNo INT(4),"
                "PRIMARY KEY (copyNo,dateOut),"
                "FOREIGN KEY (borrowerNo) REFERENCES Borrower(borrowerNO))")


    sql =   "LOAD DATA LOCAL INFILE 'Data/BookLoan.csv'"\
        "INTO TABLE BookLoan "\
        "FIELDS TERMINATED BY \',\'"\
        "ENCLOSED BY '\"'"\
        "LINES TERMINATED BY '\n'"\
        "(copyNo , dateOut, dateDue,borrowerNo)"

    print("BookLoand est crée et remplir\n")

    cur.execute(sql)
    ###############

    db.commit()


    try:
        cur.execute("DROP TABLE IF EXISTS Book_copy CASCADE ")
        cur.execute("CREATE TABLE Book_copy "
                    "(copyNo INT(4) NOT NULL AUTO_INCREMENT, "
                    "ISBN INT(4), "
                    "available VARCHAR(5) DEFAULT \"true\","
                    "PRIMARY KEY (copyNo),"
                    "FOREIGN KEY (ISBN) REFERENCES Book(ISBN))")

        cur.execute("LOAD DATA LOCAL INFILE 'Data/BookCopy.csv'"
                    "INTO TABLE Book_copy "
                    "FIELDS TERMINATED BY ','"
                    "ENCLOSED BY '\"'"
                    "LINES TERMINATED BY '\n'"
                    "(copyNo, ISBN, available)")
        db.commit()
    except:
        db.rollback()

    print("Book_copy est crée et remplir\n")

    sql = "create TRIGGER BorrowerNotHandlingTooMuch BEFORE INSERT ON BookLoan " \
          "for EACH ROW " \
          "BEGIN " \
          "IF exists (SELECT borrowerNo, count(copyNo) as nbOfCopy FROM BookLoan GROUP BY borrowerNo HAVING  nbOfCopy > 3) THEN " \
          "DELETE FROM BookLoan WHERE BookLoan.borrowerNo = NEW.borrowerNo; " \
          "END IF; " \
          "END; "

    print("Ajout du Trigger\n")


    cur.execute(sql)
    db.commit()

    cur.execute("SET FOREIGN_KEY_CHECKS=1")
    db.close()



