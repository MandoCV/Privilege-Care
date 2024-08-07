from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum, Float
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class EstatusLote(enum.Enum):
    Reservado = "Reservado"
    En_transito = "En transito"
    Recibido = "Recibido"
    Rechazado = "Rechazado"

class Lote(Base):
    __tablename__ = "tbd_lotes_medicamentos"
    
    ID = Column(Integer, primary_key=True, index=True)
    Medicamento_ID = Column(Integer, nullable=False)
    Personal_Medico_ID = Column(Integer, nullable=False)
    Clave = Column(String(20))
    Estatus = Column(Enum(EstatusLote))
    Costo_Total = Column(Float, nullable=False)
    Cantidad = Column(Integer, nullable=False)
    Ubicacion = Column(String(50))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)