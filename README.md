# 📘 Proyecto: Autenticación con FastAPI, SQLAlchemy y JWT

Este proyecto implementa un sistema de autenticación con FastAPI, SQLAlchemy y JWT (JSON Web Tokens).
Se incluyen dos métodos de login: uno mediante JSON personalizado y otro mediante OAuth2 estándar compatible con Swagger UI.

## 🚀 Tecnologías utilizadas

* FastAPI Framework para construir APIs rápidas.
* SQLAlchemy ORM para manejar la base de datos.
* PostgreSQL Base de datos relacional.
* bcrypt + passlib Hashing de contraseñas.
* PyJWT Manejo de tokens JWT.

## ⚙️ Configuración del entorno

1. Clona el repositorio
    ```bash
    git clone https://github.com/OscarPalominoC/Registro-y-Login-FastAPI.git
    cd Registro-y-Login-FastAPI
    ```
2. Crea y activa un entorno virtual
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
    ```
3. Instala dependencias
    ```bash
    pip install -r requirements.txt
    ```
4. Configura el archivo .env en la raíz del proyecto:
    ```bash
    DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/miapp
    SECRET_KEY=tu llave super secreta
    ACCESS_TOKEN_EXPIRE_MINUTES=60
    ALGORITHM=HS256
    ```
5. Ejecuta el servidor
    ```bash
    uvicorn main:app --reload
    ```
La API estará disponible en:
* 👉 http://127.0.0.1:8000
* 👉 Documentación interactiva: http://127.0.0.1:8000/docs
* 👉 Documentación interactiva: http://127.0.0.1:8000/redoc