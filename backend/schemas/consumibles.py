from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import enum

class EstatusEnum(str, enum.Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"
    En_Revision = "En Revisión"

class ConsumibleBase(BaseModel):
    Nombre: str
    Descripcion: Optional[str] = None
    Cantidad: int
    Tipo: str
    Departamento_ID: int
    Estatus: EstatusEnum = EstatusEnum.Activo
    Observaciones: Optional[str] = None
    Espacio_Medico: str

class ConsumibleCreate(ConsumibleBase):
    pass

class ConsumibleUpdate(ConsumibleBase):
    pass

class Consumible(ConsumibleBase):
    ID: int
    class Config:
        orm_mode = True
