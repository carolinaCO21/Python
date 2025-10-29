from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter(preflix="/personas", tags=["personas"])


# Entidad persona
class Persona(BaseModel):
    id:int 
    dni:str
    nombre:str
    apellidos:str
    telefono:str
    correo:str


persona_list = [
    Persona(id = 1, name= "Carolina", apellido ="Carrera", telefono="655423187", correo = "carolina@example.com"),
    Persona(id = 2, name= "Estefanía", apellido ="Martínez", telefono="653756431", correo = "estefania@example.com"),
    Persona(id = 3, name= "Berenice", apellido ="Portales", telefono="688721342", correo = "berenice@example.com"),
    Persona(id = 4, name= "Lorena", apellido ="Beltran", telefono="654211634", correo = "lorena@example.com"),
    Persona(id = 5, name= "Fernanda", apellido ="Carrera", telefono="686543214", correo = "fernando@example.com")
]


@router.get("/")
def obtener_personas():
    return persona_list


@router.get("/{id}")
def get_by_id(id_a_obtener:int):
    obtener_persona = [persona for persona in persona_list if persona.id == id_a_obtener] 
    if obtener_persona:
        return obtener_persona[0]
    raise HTTPException(status_code = 404, detail= "Persona not found")



@router.delete("/{id}")
def delete(id:int):
    obtener_persona = [persona for persona in persona_list if persona.id ==id]
    if obtener_persona:
        persona_list.remove(obtener_persona[0])
        return {}
    raise HTTPException( status_code = 404 ,detail = "Persona not found ")



#se usa solo en el post
def next_id():
    if not persona_list:
        raise HTTPException(status_code=404, detail= "Persona not found")
    return max(persona.id for persona in persona_list) +1 

#post 201 si va bien
@router.post("/", status_code =201 ,  response_modeol=Persona )
def add_persona(nueva_persona:Persona):
    if nueva_persona:
        nueva_persona.id = next_id()
        persona_list.append(nueva_persona)
        return nueva_persona

@router.put("{id}", response_model= Persona)
def mod_or_add(id:int, persona:Persona):
    if persona:
        persona.id = id
        persona_list.append(persona)
    raise HTTPException(status_code = 404, detail="Persona not found")