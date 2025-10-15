
#fastapi dev users.py


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


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


@app.get("/users")
def users():
    return users_list
                # nombre que te de la gana 
@app.get("/users/{id_user}")
def get_user(id_user:int): 
    users = [user for user in users_list if user.id == id_user]

                # len(users) lo mismo que if users
    return users[0] if users != 0 else {"error" : "No user found"}
    
   
