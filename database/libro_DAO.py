from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    @staticmethod
    def get_libri_filtrati(biblioteca: str, genere: str) -> list[Libro] | None:
        cnx = ConnessioneDB.get_connection()
        result = []
        if cnx is None:
            print("❌ Errore di connessione al database")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """
                SELECT l.*
                FROM libro l, biblioteca b 
                WHERE b.nome = COALESCE(%s,b.nome) 
                    and l.genere = COALESCE(%s,l.genere) 
                    and l.id_libro = b.id
                """
        try:
            cursor.execute(query, (biblioteca, genere,))
            for row in cursor:
                libro = Libro(
                    id=row["id"],
                    titolo=row["titolo"],
                    autore=row["autore"],
                    genere=row["genere"],
                    anno_pubblicazione=row["anno_pubblicazione"],
                    id_biblioteca=row["id_biblioteca"],
                )
                result.append(libro)
        except Exception as e:
            print(f"Errore durante la query get_libri_filtrati: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_genere() -> list[str] | None:
        cnx = ConnessioneDB.get_connection()
        result = []
        if cnx is None:
            print("❌ Errore di connessione al database")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """
                SELECT DISTINCT genere
                FROM libro
                """
        try:
            cursor.execute(query)
            for row in cursor:
                result.append(row["genere"])
        except Exception as e:
            print(f"Errore durante la query get_genere: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result