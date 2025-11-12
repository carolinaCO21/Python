
# libreria para generar el token autenticacion pip install pyjwt
# para el Hash pip install "pwdlib[argon2]"

from datetime import datetime, timedelta, timezone
from pydantic import BaseModel


# libreria para  token
import jwt

#trabajar las excepciones de los tokens
from jwt.exceptions import InvalidTokenError, PyJWTError

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
ACCESS_TOKEN_EXPIRE_MINUTES = 120

    # Clave que se utilizará como semilla para generar el token

# $  en el git bash-> openssl rand -hex 32 es el comando que usas pra obtener la clave para el token
SECRET_KEY = "bf914223caa0aca4ee088af382eeaebe72cd58b84f9fa49c4f29d2ecdca8198f"


# CONTRASEÑA

# Objeto que se utilizara para el cálculo del hash y
# la verificación de las contraseñas
password_hash = PasswordHash.recommended()


# definimos el router
from fastapi import APIRouter, Depends, HTTPException
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
    # 123456
    "prueba" : {
        "username": "prueba",
        "fullname": "Prueba Prueba",
        "email": "elenarg@prueba.es",
        "disabled": False,
        "password": "$argon2id$v=19$m=65536,t=3,p=4$7vbcfGwKOQ+rCWvT5U0eVw$W89MR7Ddnwxj7XYlbwqLgFHwteyAsVPaSBBMAiz9XNo"
    },
    #1234
    "prueba2": {
        "username": "prueba2",
        "fullname": "Prueba2 Prueba2",
        "email": "prueba2@prueba.es",
        "disabled": False,
        "password": "$argon2id$v=19$m=65536,t=3,p=4$6z7tVqDUxonwbsXtONf0bg$lJ2CNfo3rjXUYKfstpgiuUtfFuJwdPHXWTqDK9U0deU"
    }


}

@router.post("/register", status_code= 201)
def register(user : UserDB):
    if user.username not in users_db:
        hash_password = password_hash.hash(user.password)
        user.password = hash_password # machaco la contraseña de mi usuario con la del hash
        users_db[user.username] = user.model_dump()
        return user
    else:
        raise HTTPException(status_code = 409, detail = "User already exists")

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends() ):
    user_db = users_db.get(form.username)
    if  user_db:
      
        user = UserDB(**user_db)

        try:    
            # si el usuario existe en la abse de datos comprobamos la contraseña

            # user["password"]
           

            if password_hash.verify(form.password, user.password ):
                # hora actual + el tiempo de expiración del token (minutos)
                expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
                access_token = {"sub" : user.username, "exp":expire}
                # generar token
                token = jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM)
                # return token
                return {"access_token":token, "token_type": "bearer"}
        except:
            raise HTTPException(status_code=400, detail="Error al verificar la contarseña")
    raise HTTPException(status_code=401, detail="Usuario o contraseña incorrecta")

async def authentication(token: str = Depends(oauth2)):
    try:
        # decodificamos                                   sub dnd guardamos nombre de usuario 
        username = jwt.decode(token, SECRET_KEY, algorithm= ALGORITHM).get("sub")
        if not username:
            raise HTTPException(status_code=401, detail="Credenciales de autenticación inválidas" ,
            headers={"WWW-Authenticate:": "Bearer"})
    except PyJWTError:
        raise HTTPException(status_code=401, 
            detail="Credenciales de autenticacion invalidas",
            headers={"WWW-Authenticate" : "Bearer"})
    user = User(**users_db[username])
    if user.disabled:
        raise HTTPException(status_code=400, detail="Usuario inactivo")
    return user