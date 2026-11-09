from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    @staticmethod
    def get_libri(nome_biblioteca, genere):
        cnx = DBConnect.get_connection()
        risultato = []
        if cnx is None:
            print("Errore di connessione con il database")
            return None
        try:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT l.id, l.titolo, l.autore, l.genere, l.anno_pubblicazione, l.id_biblioteca
                       FROM libro l, biblioteca b
                       WHERE l.id_biblioteca = b.id
                       AND (b.nome = COALESCE(%s, b.nome))
                       AND (l.genere = COALESCE(%s, l.genere))"""
            cursor.execute(query, (nome_biblioteca, genere))
            for row in cursor:
                libro = Libro(**row)
                risultato.append(libro)
            cursor.close()
            cnx.close()
            return risultato
        except Exception as e:
            print(f"Errore durante la query {e}")
            return None

    @staticmethod
    def get_generi():
        cnx = DBConnect.get_connection()
        risultato = []
        if cnx is None:
            print("Errore di connessione con il database")
            return None
        try:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT genere
                       FROM libro"""
            cursor.execute(query)
            for row in cursor:
                if row is not None:
                    risultato.append(row['genere'])
            cursor.close()
            cnx.close()
            return risultato
        except Exception as e:
            print(f"Errore durante la query {e}")
            return None