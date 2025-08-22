import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from load_env import load_env_file

# Cargar variables de entorno (estricto)
load_env_file()

DATABASE_URL = os.environ["DATABASE_URL"]

class Base(DeclarativeBase):
    """Clase base para todos los modelos.

    Args:
        DeclarativeBase (_type_): Clase base para todos los modelos.
    """
    pass

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
