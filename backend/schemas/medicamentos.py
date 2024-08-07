from typing import Optional
from pydantic import BaseModel
from datetime import datetime
import enum

from models.medicamentos import ViaAdministracion, Presentacion, Tipo


class MedicamentoBase(BaseModel):
    Nombre_comercial: str
    Nombre_generico: str
    Via_administracion: ViaAdministracion
    Presentacion: Presentacion
    Tipo: Tipo
    Cantidad: float
    Volumen: Optional[float] = None
    Estatus: bool
    Fecha_registro: datetime
    Fecha_actualizacion: datetime

class MedicamentoCreate(MedicamentoBase):
    pass

class MedicamentoUpdate(MedicamentoBase):
    pass

class Medicamento(MedicamentoBase):
    ID: int

    class Config:
        orm_mode = True
