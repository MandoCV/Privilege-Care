from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class PersonBase(BaseModel):
    Titulo_Cortesia: str
    Nombre: str
    Primer_Apellido: str
    Segundo_Apellido: str
    Fecha_Nacimiento: datetime
    Fotografia: str
    Genero: str
    Tipo_Sangre: str
    Estatus: bool
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class PersonCreate(PersonBase):
    pass

class PersonUpdate(PersonBase):
    pass

class Person(PersonBase):
    id: int
    #owner_id: int clave foranea
    class Config:
        orm_mode = True


