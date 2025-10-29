#fastapi dev users.py

# pip install "fastapi[standard]"

#from fastapi import FastAPI, HTTPException
from fastapi import ApiRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users")


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


@router.get("/users")
def users():
    return users_list
                # nombre que te de la gana 
@router.get("/users/{id}")
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







"""
def search_user(id : int):   
    # buscamos usario por id en la lista
    # devuelve una lista vacía si no encuentra nda
    # devuelve una lista con el usuario
    users = [user for user in users_list if user.id == id]
                     # len(users) lo mismo que if users
    return users[0] if users else {"error" : "User not found"}
"""
    
   
