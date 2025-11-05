
#fastapi dev users.py

# pip install "fastapi[standard]"

#from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from fastapi import  APIRouter, HTTPException
# http://127.0.0.1:8000/docs#/ 
router = APIRouter(prefix="/users", tags=["users"])


# Entidad user
class User(BaseModel):
    id: int
    name: str
    surname:str
    age: int

# la siguiente lista pretende simular una base de datos para probar nuestra API
users_list =   [User(id=1,name = "Paco", surname="Pérez", age=30),
                User(id=2,name = "María", surname="Martínez", age=20),
                User(id=3,name = "Lucía", surname="Rodríquez", age=40) 
                ]

# sin barra ninguna para que no se confunda
#Método get con query
# http://127.0.0.1:8000/users?id=1
@router.get("")
def get_user(id : int):
    user = search_user(id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="No user found")

@router.get("/")
def users():
    return users_list
                # nombre que te de la gana 
@router.get("/{id}")
def get_user(id:int): 
    return search_user(id)



def search_user(id : int):   
    # buscamos usario por id en la lista
    # devuelve una lista vacía si no encuentra nda
    # devuelve una lista con el usuario
    users = [user for user in users_list if user.id == id]
                    # len(users) == 0 ? lo mismo que if users
    if not  users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[0]


def next_id():
# Calculamos el usuario con el id más alto
# y le sumamos 1 a su id
# esto te devuelve el id maximo y le sumamos 1
# 'key=lambda user: user.id' indica que la comparación se haga por el atributo .id
    return max(users_list, key=lambda user: user.id).id + 1


# POST status_code= 201 si va bien
                                        # le masamos una clase para append
@router.post("/", status_code=201, response_model=User)
def add_user(user: User):
    # Calculamos nuevo id y lo modificamos al usuario a añadir
    user.id = next_id()
    # Añadimos el usuario a nuestra lista
    users_list.append(user)
    # La respuesta de nuestro método es el propio usuario añadido
    return user



@router.put("/{id}", response_model=User)
def modify_user(id: int, user: User):
    # El método enumerate devuelve el índice de la lista
    # y el usuario almacenado en dicho índice
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            user.id = id
            users_list[index] = user
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{id}")
def remove_user(id: int):
    for saved_user in users_list:
        if saved_user.id == id:
            users_list.remove(saved_user)
            return {}
    raise HTTPException(status_code=404, )

"""
def search_user(id : int):   
    # buscamos usario por id en la lista
    # devuelve una lista vacía si no encuentra nda
    # devuelve una lista con el usuario
    users = [user for user in users_list if user.id == id]
                    # len(users) lo mismo que if users
    return users[0] if users else {"error" : "User not found"}
"""