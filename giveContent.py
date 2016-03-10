import sqlite3 as lite

def recupLivres(patronRecherche):

    con = lite.connect("TP2.db")

    with con:
        patron = (patronRecherche,)
        cur = con.execute("SELECT * FROM Livres WHERE nomLivre LIKE '%'+ ? +'%'", patron) #marche pas

        for row in cur:
            print("[Nom du livre:]",row[1], "[Nom de l'auteur:]",row[2], "[ISBN:]",row[3], "[Date de publication:]",row[4])