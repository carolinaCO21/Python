#fastapi dev tiendas.py


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# ojito Entidad 
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

                # len(lista) lo mismo que if lista
    return tienda_busqueda[0] if tienda_busqueda != 0 else {"error" : "No user found"}
    

def next_id():
    if not tiendas_list: 
        raise ValueError("Lista de tiendas vacia")
    max_id:int =  max(tienda.id for tienda in tiendas_list)
    return max_id+1


#201 si va bien
@app.post("/tiendas", status_code=201, response_model=Tienda)
def add_tienda(nueva_tienda:Tienda):
    nueva_tienda.id = next_id()
    tiendas_list.append(nueva_tienda)
    return nueva_tienda

@app.put("/tiendas/{id}", response_model=Tienda)
def modify_tienda(id:int, tienda_mod_or_add:Tienda):
    for index, tienda in enumerate(tiendas_list):
        if tienda.id == id:
            tiendas_list[index] = tienda_mod_or_add
            return tienda_mod_or_add
    raise HTTPException(status_code=404, detail="tienda not found")



@app.delete("/tiendas/{id}")
def remove_tiendas(id: int):
    for saved_tienda in tiendas_list:
        if saved_tienda.id == id:
            tiendas_list.remove(saved_tienda)
            return {}
    raise HTTPException(status_code=404, )