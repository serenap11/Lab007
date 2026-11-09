from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    @staticmethod
    def get_biblioteche():
        cnx = DBConnect.get_connection()
        risultato = []
        if cnx is None:
            print("Errore di connessione con il database")
            return None
        try:
            cursor = cnx.cursor(dictionary=True)
            query = "SELECT * FROM biblioteca"
            cursor.execute(query)
            for row in cursor:
                biblioteca = Biblioteca(**row)
                risultato.append(biblioteca)
            cursor.close()
            cnx.close()
            return risultato
        except Exception as e:
            print(f"Errore durante la query {e}")
            return None