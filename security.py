import os
from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext
from load_env import load_env_file

# Cargar variables de entorno (estricto)
load_env_file()

SECRET_KEY = os.environ["SECRET_KEY"]
ALGORITHM = os.environ["ALGORITHM"]
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """
    Genera un hash seguro para una contraseña en texto plano.

    Usa el algoritmo bcrypt con los parámetros definidos en `pwd_context`.

    Args:
        password (str): Contraseña en texto plano.

    Returns:
        str: Hash de la contraseña.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, password_hash: str) -> bool:
    """
    Verifica si una contraseña en texto plano coincide con un hash almacenado.

    Args:
        plain_password (str): Contraseña proporcionada por el usuario.
        password_hash (str): Hash previamente almacenado en la base de datos.

    Returns:
        bool: True si la contraseña es válida, False en caso contrario.
    """
    return pwd_context.verify(plain_password, password_hash)

def create_access_token(subject: str) -> str:
    """
    Crea un token de acceso JWT para un usuario autenticado.

    Args:
        subject (str): Identificador del usuario (usualmente el ID).

    Returns:
        str: Token de acceso JWT.
    """
    expire = datetime.now(tz=timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": subject, "exp": expire}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
