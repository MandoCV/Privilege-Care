from typing import List, Optional, Union
from pydantic import BaseModel
from datetime import datetime

from models.lotes import EstatusLote

class LoteBase(BaseModel):
    Medicamento_ID: int
    Personal_Medico_ID: int
    Clave: str
    Estatus: EstatusLote
    Costo_Total: float
    Cantidad: int
    Ubicacion: str
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class LoteCreate(LoteBase):
    pass

class LoteUpdate(BaseModel):
    Clave: Optional[str] = None
    Estatus: Optional[EstatusLote] = None
    Costo_Total: Optional[float] = None
    Cantidad: Optional[int] = None
    Ubicacion: Optional[str] = None
    Fecha_Registro: Optional[datetime] = None
    Fecha_Actualizacion: Optional[datetime] = None

class Lote(LoteBase):
    ID: int
    class Config:
        orm_mode = True