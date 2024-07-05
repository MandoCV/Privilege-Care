from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

person = APIRouter()
persons = []

#personsModel
class model_person(BaseModel):
    id:str
    nombre:str
    primer_apellido: str
    segundo_apellido: str
    direccion: str
    telefono: str
    correo: str
    sangre: str
    fecha_nacimiento: datetime
    created_at:datetime = datetime.now()
    estatus:bool=False

@person.get('/')

def bienvenida():
    return "Bienvenido al sistema de apis"

@person.get('/persons', tags=["Personas"])

def get_personas():
    return persons

@person.post('/persons', tags=["Personas"] )

def save_personas(insert_persons:model_person):
    persons.append(insert_persons)
    print (insert_persons)
    return "Datos guardados"

@person.post('/person/{person_id}', tags=["Personas"])

def get_persona(person_id: str):
    for person in persons:
        if person.id== person_id:
            return person
    return "No existe el registro"

@person.delete('/person/{person_id}', tags=["Personas"])

def delete_persona(person_id: str):
    for person in persons:
        if person.id == person_id:
            persons.remove(person)
            return "Registro eliminado correctamente"
    return "Registro no encontrado"

@person.put('/person/{person_id}', tags=["Personas"])

def update_persona(person_id: str, updateperson: model_person):
    for person in persons:
        if person.id == person_id:
            person.nombre=updateperson.nombre
            person.primer_apellido=updateperson.primer_apellido
            person.segundo_apellido=updateperson.segundo_apellido
            person.direccion=updateperson.direccion
            person.telefono=updateperson.telefono
            person.correo=updateperson.correo
            person.sangre=updateperson.sangre
            person.fecha_nacimiento=updateperson.fecha_nacimiento
            person.estatus=updateperson.estatus
            return "Registro actualizado correctamente"
    return "Registro no encontrado"