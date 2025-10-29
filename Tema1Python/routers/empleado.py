
# fastapi dev empleado.py 

#pip install "fastapi[standart]"

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/empleados", tags=["empleados"])


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
    Empleado(id=2, nombre="Marta",apellidos="Pérez Perez",telefono= "633852354",correo="paco@example.com", num_cuenta="P-02", id_tienda=1 ),
    Empleado(id=3, nombre="Jose",apellidos="Pérez Fernández",telefono= "633852354",correo="paco@example.com", num_cuenta="P-03", id_tienda=1 ),
    Empleado(id=4, nombre="Nuria",apellidos="Pérez Muños",telefono= "633852354",correo="paco@example.com", num_cuenta="P-04", id_tienda=1 )

]

@router.get("/empleados")
def obtener_empleados():
    return empleados_list

@router.get("/empleados/{id}")
def obtener_empleado_por_id(id:int):
    return search_empleado(id)



def search_empleado(id_a_encontrar):
    empleado_busqueda = [empleado for empleado in empleados_list if empleado.id == id_a_encontrar]
    if empleado_busqueda:
        return empleado_busqueda[0] 
    raise HTTPException(status_code=404, detail="Empleado no encontrado")

def next_id():
    if not empleados_list: 
        raise ValueError("Lista de empleados vacia")
    max_id:int =  max(empleado.id for empleado in empleados_list)
    return max_id+1

#201 si va bien
@router.post("/empleados", status_code=201, response_model=Empleado)
def add_empleado(nuevo_empleado:Empleado):
    nuevo_empleado.id = next_id()
    empleados_list.append(nuevo_empleado)
    return nuevo_empleado

@router.put("/empleados/{id}", response_model=Empleado)
def modify_empleado(id:int, empleado_mod_or_add:Empleado):
    for index, empleado in enumerate(empleados_list):
        if empleado.id == id:
            empleados_list[index] = empleado_mod_or_add
            return empleado_mod_or_add
    raise HTTPException(status_code=404, detail="Empleado not found")

@router.delete("/empleados/{id}")
def remove_empleado(id: int):
    for saved_empleado in empleados_list:
        if saved_empleado.id == id:
            empleados_list.remove(saved_empleado)
            return {}
    raise HTTPException(status_code=404, detail="Empleado not found")