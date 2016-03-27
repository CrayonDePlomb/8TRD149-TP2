#!/usr/bin/python
# -*- coding: utf-8 -*-
import mysql.connector

user = "root"
password = "root678"
database = "tp2db"

def create():


    db = mysql.connector.connect(user=user, password=password, database=database)

    cur = db.cursor()



    cur.execute("SET FOREIGN_KEY_CHECKS=0") # Il ne regarde plus les foreign_key

# CREATION TABLE BOOK
    cur.execute("DROP TABLE IF EXISTS Book Cascade")
    cur.execute("CREATE TABLE Book "
                "(ISBN INT PRIMARY KEY NOT NULL, "
                "title VARCHAR(255) UNIQUE NOT NULL,"
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

# CREATION TABLE BOOK_COPY
    cur.execute("DROP TABLE IF EXISTS Book_copy CASCADE ")
    cur.execute("CREATE TABLE Book_copy "
                    "(copyNo INT(4) NOT NULL AUTO_INCREMENT, "
                    "ISBN INT(4) NOT NULL, "
                    "available BOOLEAN NOT NULL DEFAULT TRUE,"
                    "PRIMARY KEY (copyNo),"
                    "FOREIGN KEY (ISBN) REFERENCES Book(ISBN))"
                    )

    cur.execute("LOAD DATA LOCAL INFILE 'Data/BookCopy.csv'"
                    "INTO TABLE Book_copy "
                    "FIELDS TERMINATED BY ','"
                    "ENCLOSED BY '\"'"
                    "LINES TERMINATED BY '\n'"
                    "(copyNo, ISBN, available)")
    db.commit()

    print("Book_copy est crée et remplir\n")

# CREATION TABLE BORROWER
    cur.execute("DROP TABLE IF EXISTS Borrower CASCADE ")
    cur.execute("CREATE TABLE Borrower "
                "(borrowerNo INT(4) NOT NULL AUTO_INCREMENT, "
                "borrowerName VARCHAR(255) NOT NULL UNIQUE , "
                "borrowerAddress VARCHAR(255),"
                "PRIMARY KEY (borrowerNo))")

    cur.execute("LOAD DATA LOCAL INFILE 'Data/Borrower.csv'"
                "INTO TABLE Borrower "
                "FIELDS TERMINATED BY ','"
                "ENCLOSED BY '\"'"
                "LINES TERMINATED BY '\n'"
                "(borrowerNo, borrowerName, BorrowerAddress)")
    db.commit()

    print("Borrower est crée et remplir\n")

# CREATION TABLE BOOKLOAN
    cur.execute("DROP TABLE IF EXISTS BookLoan CASCADE ")
    cur.execute("CREATE TABLE BookLoan "
                "(copyNo INT(4) NOT NULL , "
                "dateOut DATE NOT NULL, "
                "dateDue DATE NOT NULL,"
                "borrowerNo INT(4) NOT NULL,"
                "PRIMARY KEY (copyNo,dateOut),"
                "FOREIGN KEY (copyNo) REFERENCES book_copy(copyNo),"
                "FOREIGN KEY (borrowerNo) REFERENCES Borrower(borrowerNo))")

    cur.execute("LOAD DATA LOCAL INFILE 'Data/BookLoan.csv'"\
        "INTO TABLE BookLoan "\
        "FIELDS TERMINATED BY \',\'"\
        "ENCLOSED BY '\"'"\
        "LINES TERMINATED BY '\n'"\
        "(copyNo , dateOut, dateDue,borrowerNo)")
    db.commit()

    print("BookLoan est crée et remplir\n")

# CREATION TRIGGER BORROWER NOT LOANING MORE THAN 3 BOOKS
    sql = "CREATE TRIGGER BorrowerNotHandlingTooMuch BEFORE INSERT ON BookLoan " \
          "FOR EACH ROW " \
          "BEGIN " \
          "IF EXISTS (SELECT borrowerNo, COUNT(copyNo) AS nbOfCopy FROM BookLoan WHERE BookLoan.borrowerNo = NEW.borrowerNo GROUP BY borrowerNo HAVING  nbOfCopy > 3) " \
          "AND "' . NEW.dateOut . '" BETWEEN "' . BookLoan.dateOut . '" AND "' . BookLoan.dateDue . '" " \
          "THEN DELETE FROM BookLoan WHERE BookLoan.borrowerNo = NEW.borrowerNo; " \
          "END IF; " \
          "END; "

    cur.execute(sql)
    db.commit()

    print("Ajout du Trigger BorrowerNotHandlingTooMuch\n")

# CREATION TRIGGER BORROWER NOT LOANING BOOK UNVAILABLE AT DATE
    sql = "CREATE TRIGGER BookLoanNotInDate BEFORE INSERT ON BookLoan " \
          "FOR EACH ROW " \
          "BEGIN " \
          "IF EXISTS (SELECT * FROM BookLoan WHERE BookLoan.borrowerNo = NEW.borrowerNo) " \
          "AND "' . NEW.dateOut . '" BETWEEN "' . BookLoan.dateOut . '" AND "' . BookLoan.dateDue . '" " \
          "THEN DELETE FROM BookLoan WHERE BookLoan.borrowerNo = NEW.borrowerNo; " \
          "END IF; "\
          "END; "\

    cur.execute(sql)
    db.commit()

    print("Ajout du Trigger BookLoanNotInDate\n")

    cur.execute("SET FOREIGN_KEY_CHECKS=1")
    db.close()



0