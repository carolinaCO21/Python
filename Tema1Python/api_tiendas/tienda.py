#fastapi dev tiendas.py


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# ojito Entidad user
class Tienda(BaseModel):
    id: int
    domicilio: str
    telefono:str
    precio_alquiler: float

# "la siguiente lista pretende simular una base de datos para probar nuestra API" diapositivas
tiendas_list =   [Tienda(id=1,domicilio="Calle Mayor 12", telefono="912345678", precio_alquiler=1200.50),
                Tienda(id=2,domicilio="Avenida Sur 5", telefono="650112233", precio_alquiler=850.00),
                Tienda(id=3, domicilio="Plaza Central 4", telefono="931002003", precio_alquiler=2500.99)
                ]


@app.get("/tiendas")
def tiendas():
    return tiendas_list
                
@app.get("/tiendas/{id_tienda}")
def get_tienda(id_tienda:int): 
    tienda_busqueda= [tienda for tienda in tiendas_list if tienda.id == id_tienda]

                # len(users) lo mismo que if users
    return tienda_busqueda[0] if tienda_busqueda != 0 else {"error" : "No user found"}
    