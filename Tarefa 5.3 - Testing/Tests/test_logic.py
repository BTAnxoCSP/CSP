import unittest
from app.logic import crear_pelicula, buscar_pelicula, actualizar_nota_y_vista

class TestLogicCine(unittest.TestCase):
    """
    Clase para realizar as probas unitarias das funcións de lóxica da app de cine.
    """

    def setUp(self):
        """Prepara un catálogo de proba antes de cada test."""
        self.catalogo_proba = [
            {"titulo": "Inception", "director": "Christopher Nolan", "anho": 2010, "genero": "Sci-Fi", "puntuacion": 9.0, "vista": True},
            {"titulo": "Avatar", "director": "James Cameron", "anho": 2009, "genero": "Sci-Fi", "puntuacion": None, "vista": False}
        ]

    def test_crear_pelicula(self):
        """Proba que a creación de películas devolve o dicionario cos campos correctos."""
        nueva = crear_pelicula("Jurassic Park", "Steven Spielberg", 1993, "Sci-Fi")
        self.assertEqual(nueva["titulo"], "Jurassic Park")
        self.assertFalse(nueva["vista"])
        self.assertIsNone(nueva["puntuacion"])

    def test_buscar_pelicula_existente(self):
        """Proba que se atopa unha película polo título (sen importar maiúsculas)."""
        indice = buscar_pelicula(self.catalogo_proba, "INCEPTION")
        self.assertEqual(indice, 0)

    def test_buscar_pelicula_non_existente(self):
        """Proba que devolve -1 se a película non está no catálogo."""
        indice = buscar_pelicula(self.catalogo_proba, "Titanic")
        self.assertEqual(indice, -1)

    def test_actualizar_nota(self):
        """Proba que se marca como vista e se asigna a nota correctamente."""
        actualizar_nota_y_vista(self.catalogo_proba, 1, 8.5)
        self.assertTrue(self.catalogo_proba[1]["vista"])
        self.assertEqual(self.catalogo_proba[1]["puntuacion"], 8.5)

if __name__ == '__main__':
    unittest.main()