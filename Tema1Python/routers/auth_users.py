
# libreria para generar el token autenticacion pip install pyjwt
# para el Hash pip install "pwdlib[argon2]"

from pydantic import BaseModel


# libreria para  token
import jwt
#trabajar las excepciones de los tokens
from jwt.exceptions import InvalidTokenError

# Librería para aplicar un hash a la contraseña
from pwdlib import PasswordHash
                            #  gestiona la autenticción  2.-  el formulario
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

                            # path para la autenticación
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# TOKEN

    # definimos algoritmo para cifrar el token -> nombre
ALGORITHM = "HS256"

    # Duración del token
ACCESS_TOKEN_EXPIRE_MINUTES = 5

    # Clave que se utilizará como semilla para generar el token

# $  en el git bash-> openssl rand -hex 32 es el comando que usas pra obtener la clave para el token
SECRET_KEY = "bf914223caa0aca4ee088af382eeaebe72cd58b84f9fa49c4f29d2ecdca8198f"


# CONTRASEÑA

# Objeto que se utilizara para el cálculo del hash y
# la verificación de las contraseñas
password_hash = PasswordHash.recommended()


# definimos el router
from fastapi import APIRouter, HTTPException
router = APIRouter()


class User(BaseModel):
    username : str
    fullname : str
    email: str
    disabled : bool

class UserDB(User):
    password: str

users_db = {
    "elenarg": {
        "username" : "elenarg",
        "fullname" : "Elena Rivero",
        "email": "elenarg@prueba.es",
        "disabled": False, 
        "password" : "123456"

    },
    "prueba" : {
        "username": "prueba",
        "fullname": "Prueba Prueba",
        "email": "elenarg@prueba.es",
        "disabled": False,
        "password": "$argon2id$v=19$m=65536,t=3,p=4$7vbcfGwKOQ+rCWvT5U0eVw$W89MR7Ddnwxj7XYlbwqLgFHwteyAsVPaSBBMAiz9XNo"
    }


}

@router.post("/registrar", status_code= 201)
def register(user : UserDB):
    if user.username not in users_db:
        hash_password = password_hash.hash(user.password)
        user.password = hash_password # machaco la contraseña de mi usuario con la del hash
        users_db[user.username] = user
        return user
    else:
        raise HTTPException(status_code = 409, detail = "User already exists")

"""
le pasamos en el post por ejemplo
{
        "username" : "prueba",
        "fullname" : "Prueba Prueba",
        "email": "elenarg@prueba.es",
        "disabled": false, 
        "password" : "123456"

}




"""