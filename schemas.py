from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    """Esquema para la creación de un usuario.

    Args:
        BaseModel (type): Clase base para la validación de datos.
    """
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    first_name: str = Field(min_length=1, max_length=100)
    last_name: str = Field(min_length=1, max_length=100)

class UserOut(BaseModel):
    """Esquema para la salida de datos del usuario (sin contraseña).

    Args:
        BaseModel (type): Clase base para la validación de datos.
    """
    id: int
    email: EmailStr
    first_name: str
    last_name: str

    class Config:
        """Configuración del modelo."""
        from_attributes = True

class LoginRequest(BaseModel):
    """Esquema para la solicitud de inicio de sesión.

    Args:
        BaseModel (type): Clase base para la validación de datos.
    """
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)

class Token(BaseModel):
    """Esquema para la representación de un token JWT.

    Args:
        BaseModel (type): Clase base para la validación de datos.
    """
    access_token: str
    token_type: str = "bearer"
