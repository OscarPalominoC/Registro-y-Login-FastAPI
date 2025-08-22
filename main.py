from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy import select

from database import SessionLocal, engine, Base
from models import User
from schemas import UserCreate, UserOut, LoginRequest, Token
from security import get_password_hash, verify_password, create_access_token

app = FastAPI(title="Auth API (FastAPI + PostgreSQL)")

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

def get_db():
    """Obtiene una sesión de base de datos.

    Yields:
        Session: Una sesión de base de datos.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------- Registro ----------
@app.post("/auth/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    """
    Registra un nuevo usuario en la base de datos.

    Args:
        user_in (UserCreate): Datos del usuario a registrar.
        db (Session, optional): Sesión de base de datos. Por defecto se obtiene de la dependencia.

    Raises:
        HTTPException: Si el correo ya está registrado.

    Returns:
        UserOut: Datos del usuario registrado.
    """
    existing = db.scalar(select(User).where(User.email == user_in.email))
    if existing:
        raise HTTPException(status_code=400, detail="El correo ya está registrado.")

    user = User(
        email=user_in.email,
        first_name=user_in.first_name.strip(),
        last_name=user_in.last_name.strip(),
        password_hash=get_password_hash(user_in.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# ---------- Login ----------
@app.post("/auth/login", response_model=Token)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    """
    Inicia sesión para un usuario existente.

    Args:
        payload (LoginRequest): Datos de inicio de sesión.
        db (Session, optional): Sesión de base de datos. Por defecto se obtiene de la dependencia.

    Raises:
        HTTPException: Si las credenciales son inválidas.

    Returns:
        Token: Token de acceso JWT.
    """
    user = db.scalar(select(User).where(User.email == payload.email))
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas.")
    token = create_access_token(subject=str(user.id))
    return Token(access_token=token)

# ---------- Login OAuth2 ----------
@app.post("/auth/token", response_model=Token)
def login_oauth2(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Inicia sesión para un usuario existente utilizando OAuth2.

    Args:
        form_data (OAuth2PasswordRequestForm, optional): Datos de inicio de sesión. Por defecto se obtiene de la dependencia.
        db (Session, optional): Sesión de base de datos. Por defecto se obtiene de la dependencia.

    Raises:
        HTTPException: Si las credenciales son inválidas.

    Returns:
        Token: Token de acceso JWT.
    """
    user = db.scalar(select(User).where(User.email == form_data.username))
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas.")
    token = create_access_token(subject=str(user.id))
    return Token(access_token=token)
