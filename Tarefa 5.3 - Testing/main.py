"""
Script principal main.py
Inicia a aplicación 'Mi Videoteca Personal'. Controla o menú interactivo
e coordina as chamadas aos módulos de lóxica e entrada/saída.
"""

from app.io import cargar_datos, guardar_datos
from app.logic import (crear_pelicula, buscar_pelicula, actualizar_nota_y_vista, eliminar_pelicula, editar_pelicula)

RUTA_JSON = "data/peliculas.json"

def mostrar_menu():
    """
    Imprime por consola as opcións dispoñibles para o usuario.
    Móstrase visualmente con separadores para facilitar a lectura.
    """
    print("\n" + "=" * 30)
    print("🎬 MI VIDEOTECA PERSONAL")
    print("=" * 30)
    print("1. Ver catálogo")
    print("2. Añadir película pendiente")
    print("3. Editar datos (Título, Nota, etc.)")
    print("4. ¡Ya la he visto! (Puntuar)")
    print("5. Eliminar película")
    print("6. Buscar detalles")
    print("7. Guardar y Salir")

def ejecutar_app():
    """
    Controla o ciclo de vida principal da aplicación.
    Carga os datos dende o JSON, xestiona os inputs do usuario nun bucle
    e asegura que os datos se garden antes de saír.
    """
    catalogo = cargar_datos(RUTA_JSON)

    while True:
        mostrar_menu()
        opcion = input("\nSelecciona: ")

        if opcion == "1":
            print("\n--- CATÁLOGO ---")
            if not catalogo: print("El catálogo está vacío.")
            for p in catalogo:
                estado = "✅" if p["vista"] else "⏳"
                nota = f"⭐ {p['puntuacion']}/10" if p["puntuacion"] is not None else "--- (Sin nota)"
                print(f"{estado} {p['titulo'].upper()} | {nota}")

        elif opcion == "2":
            try:
                t, d = input("Título: "), input("Director: ")
                a, g = int(input("Año: ")), input("Género: ")
                catalogo.append(crear_pelicula(t, d, a, g))
                print("✨ Añadida a pendientes.")
            except ValueError:
                print("❌ Error: El año debe ser un número.")

        elif opcion == "3":
            nombre = input("Película a editar: ")
            idx = buscar_pelicula(catalogo, nombre)
            if idx != -1:
                try:
                    peli = catalogo[idx]
                    print(f"Editando: {peli['titulo']}")
                    nuevos_datos = {
                        "titulo": input(f"Nuevo título [{peli['titulo']}]: ") or peli['titulo'],
                        "director": input(f"Nuevo director [{peli['director']}]: ") or peli['director'],
                        "anho": int(input(f"Nuevo año [{peli['anho']}]: ") or peli['anho']),
                        "genero": input(f"Nuevo género [{peli['genero']}]: ") or peli['genero']
                    }
                    # Si ya está vista, permitimos editar la nota
                    if peli["vista"]:
                        nota_input = input(f"Nueva nota [{peli['puntuacion']}]: ")
                        nuevos_datos["puntuacion"] = float(nota_input) if nota_input else peli['puntuacion']

                    editar_pelicula(catalogo, idx, nuevos_datos)
                    print("✅ Cambios guardados.")
                except ValueError:
                    print("❌ Error en los datos introducidos.")
            else:
                print("🔍 No encontrada.")

        elif opcion == "4":
            nombre = input("¿Qué película has visto?: ")
            idx = buscar_pelicula(catalogo, nombre)
            if idx != -1:
                try:
                    nota = float(input("¿Qué nota le das (0-10)?: "))
                    if 0 <= nota <= 10:
                        actualizar_nota_y_vista(catalogo, idx, nota)
                        print(f"✅ ¡Hecho! Has puntuado '{catalogo[idx]['titulo']}'.")
                    else:
                        print("❌ La nota debe ser de 0 a 10.")
                except ValueError:
                    print("❌ Entrada no válida.")
            else:
                print("🔍 No encontrada.")

        elif opcion == "5":
            nombre = input("Título a borrar: ")
            idx = buscar_pelicula(catalogo, nombre)
            if idx != -1:
                eliminar_pelicula(catalogo, idx)
                print("🗑️ Eliminada.")
            else:
                print("🔍 No encontrada.")

        elif opcion == "6":
            nombre = input("Buscar detalles de: ")
            idx = buscar_pelicula(catalogo, nombre)
            if idx != -1:
                p = catalogo[idx]
                nota_display = f"{p['puntuacion']}/10" if p['puntuacion'] is not None else "No puntuada"
                print(f"\n--- {p['titulo'].upper()} ---")
                print(f"Director: {p['director']} | Año: {p['anho']} | Género: {p['genero']}")
                print(f"Estado: {'✅ VISTA' if p['vista'] else '⏳ PENDIENTE'} | Nota: {nota_display}")
            else:
                print("🔍 No encontrada.")

        elif opcion == "7":
            guardar_datos(RUTA_JSON, catalogo)
            print("💾 Datos guardados. ¡Adiós!")
            break

if __name__ == "__main__":
    ejecutar_app()