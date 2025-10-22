
# fastapi dev empleado.py 

#pip install "fastapi[standart]"

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


#Entidad Empleado
class Empleado(BaseModel):
    id:int
    nombre:str
    apellidos:str
    telefono:str
    correo:str
    num_cuenta:str
    id_tienda:int

empleados_list = [
    Empleado(id=1, nombre="Paco",apellidos="Pérez Martínez",telefono= "633852354",correo="paco@example.com", num_cuenta="P-01", id_tienda=1 ),
    Empleado(id=2, nombre="Marta",apellidos="Pérez Perez",telefono= "633852354",correo="paco@example.com", num_cuenta="P-01", id_tienda=1 ),
    Empleado(id=3, nombre="Jose",apellidos="Pérez Fernández",telefono= "633852354",correo="paco@example.com", num_cuenta="P-01", id_tienda=1 ),
    Empleado(id=4, nombre="Nuria",apellidos="Pérez Muños",telefono= "633852354",correo="paco@example.com", num_cuenta="P-01", id_tienda=1 )

]

@app.get("/empleados")
def obtener_empleados():
    return empleados_list

@app.get("/empleados/{id}")
def obtener_empleado_por_id(id:int):
    return search_empleado(id)



def search_empleado(id_a_encontrar):
    for empleado in empleados_list:
        if empleado.id == id_a_encontrar:
            return empleado
    raise HTTPException(status_code=404, detail="Empleado not found")

def next_id():
    if not empleados_list: 
        raise ValueError("Lista de empleados vacia")
    max_id:int =  max(empleado.id for empleado in empleados_list)
    return max_id+1

#201 si va bien
@app.post("/users", status_code=201, response_model=Empleado)
def add_empleado(empleado_a_Añadir:Empleado):
    empleado_a_Añadir.id = next_id()
    empleados_list.append(empleado_a_Añadir)
    return empleado_a_Añadir

@app.put("/empleados/{id}", response_model=Empleado)
def modify_empleado(id:int, empleado_mod_or_add:Empleado):
    for index, empleado in enumerate(empleados_list):
        if empleado.id == id:
            empleados_list[index] = empleado_mod_or_add
            return empleado_mod_or_add
    raise HTTPException(status_code=404, detail="User not found")

