"""
Módulo logic.py
Contén a lóxica de negocio para a xestión do catálogo de películas.
Define as operacións de creación, busca, edición e borrado.
"""

def crear_pelicula(titulo: str, director: str, anho: int, genero: str) -> dict:
    """
    Crea un dicionario que representa unha película pendente de ver.

    Args:
        titulo (str): O título da película.
        director (str): O nome do director.
        anho (int): O ano de estrea.
        genero (str): O xénero cinematográfico.

    Returns:
        dict: Un dicionario co estado inicial (sen nota e non vista).
    """
    return {
        "titulo": titulo,
        "director": director,
        "anho": anho,
        "genero": genero,
        "puntuacion": None,
        "vista": False
    }

def buscar_pelicula(catalogo: list, titulo: str) -> int:
    """
    Busca unha película polo seu título dentro da lista do catálogo.

    Args:
        catalogo (list): Lista de dicionarios de películas.
        titulo (str): Cadea de texto co título a buscar.

    Returns:
        int: O índice da película se existe, ou -1 se non se atopa.
    """
    for i, peli in enumerate(catalogo):
        if peli["titulo"].lower() == titulo.lower():
            return i
    return -1

def actualizar_nota_y_vista(catalogo: list, indice: int, nota: float) -> None:
    """
    Marca unha película como vista e asígnalle unha puntuación.

    Args:
        catalogo (list): Lista de películas.
        indice (int): Posición da película no catálogo.
        nota (float): Puntuación numérica do 0 ao 10.
    """
    catalogo[indice]["vista"] = True
    catalogo[indice]["puntuacion"] = nota

def editar_pelicula(catalogo: list, indice: int, datos_nuevos: dict) -> None:
    """
    Actualiza os datos dunha película existente cos novos valores proporcionados.

    Args:
        catalogo (list): Lista de películas.
        indice (int): Posición da película a editar.
        datos_nuevos (dict): Dicionario cos campos actualizados.
    """
    catalogo[indice].update(datos_nuevos)

def eliminar_pelicula(catalogo: list, indice: int) -> None:
    """
    Elimina permanentemente unha película do catálogo.

    Args:
        catalogo (list): Lista de películas.
        indice (int): Posición do elemento a eliminar.
    """
    catalogo.pop(indice)