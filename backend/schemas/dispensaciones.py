from typing import Optional
from pydantic import BaseModel
from datetime import datetime
import enum

from models.dispensaciones import Estatus, Tipo

class DispensacionBase(BaseModel):
    RecetaMedica_id: int
    PersonalMedico_id: int
    Solicitud_id: int
    Estatus: Estatus
    Tipo: Tipo
    TotalMedicamentosEntregados: int
    Total_costo: float
    Fecha_registro: datetime
    Fecha_actualizacion: datetime

class DispensacionCreate(DispensacionBase):
    pass

class DispensacionUpdate(BaseModel):
    RecetaMedica_id: Optional[int] = None
    PersonalMedico_id: Optional[int] = None
    Solicitud_id: Optional[int] = None
    Estatus: Optional[Estatus] = None
    Tipo: Optional[Tipo] = None
    TotalMedicamentosEntregados: Optional[int] = None
    Total_costo: Optional[float] = None
    Fecha_registro: Optional[datetime] = None
    Fecha_actualizacion: Optional[datetime] = None

class Dispensacion(DispensacionBase):
    ID: int

    class Config:
        orm_mode = True
