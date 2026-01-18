# 🎬 Gestor de Videoteca Personal - ECP

## 👤 Autor
- **Nombre:** Anxo Barral Taboada
- **Centro:** IES San Clemente
- **Fecha:** Enero 2026

## 🔗 GitHub
Puedes ver el código y el historial de versiones aquí:
- **Repositorio:** https://github.com/BTAnxoCSP/Proyecto_ECP_CineApp

## 📝 Descripción
Esta aplicación permite gestionar un catálogo de películas pendientes y vistas. 
- Las películas se añaden inicialmente como **pendientes** y sin nota.
- Al marcarlas como **vistas**, el sistema solicita una puntuación personal.
- Permite editar cualquier dato (título, director, año, género e incluso la nota).
- Los datos se guardan de forma persistente en un archivo JSON.

## 📂 Estructura del Proyecto
El código sigue una estructura modular para cumplir con los requisitos de la asignatura:
- `main.py`: Punto de entrada de la aplicación y gestión del menú.
- `app/logic.py`: Contiene toda la lógica de negocio (CRUD).
- `app/io.py`: Gestiona la lectura y escritura del archivo JSON.
- `data/peliculas.json`: Base de datos del proyecto.

## 🚀 Instalación y Uso
1. Asegúrate de tener Python 3.10 o superior.
2. Ejecuta la aplicación con:
   ```bash
   python main.py