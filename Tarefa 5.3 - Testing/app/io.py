"""
Módulo io.py
Xestiona a entrada/saída de datos mediante o sistema de arquivos.
Encárgase da persistencia en formato JSON.
"""
import json
import os

def cargar_datos(ruta: str) -> list:
    """
    Carga a lista de películas desde un arquivo JSON.

    Args:
        ruta (str): Camiño relativo ou absoluto ao arquivo .json.

    Returns:
        list: Lista de dicionarios coas películas cargadas ou baleira se hai erro.
    """
    try:
        if not os.path.exists(ruta):
            return []
        with open(ruta, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("⚠️ Error al leer la base de datos. Iniciando lista vacía.")
        return []

def guardar_datos(ruta: str, datos: list) -> None:
    """
    Garda a lista de películas no disco en formato JSON.

    Args:
        ruta (str): Camiño ao arquivo .json de destino.
        datos (list): Lista de dicionarios que se desexa persistir.
    """
    try:
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"❌ No se pudieron guardar los datos: {e}")