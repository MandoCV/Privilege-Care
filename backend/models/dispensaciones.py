from sqlalchemy import Column, Integer, Enum, Float, DateTime
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class Estatus(enum.Enum):
    Abastecida = "Abastecida"
    Parcialmente_abastecida = "Parcialmente abastecida"

class Tipo(enum.Enum):
    Publica = "Pública"
    Privada = "Privada"
    Mixta = "Mixta"

class Dispensacion(Base):
    __tablename__ = "tbd_dispensaciones"
    
    ID = Column(Integer, primary_key=True, index=True)
    RecetaMedica_id = Column(Integer, nullable=False)
    PersonalMedico_id = Column(Integer, nullable=False)
    Solicitud_id = Column(Integer, nullable=False)
    Estatus = Column(Enum(Estatus))
    Tipo = Column(Enum(Tipo))
    TotalMedicamentosEntregados = Column(Integer, nullable=False)
    Total_costo = Column(Float)
    Fecha_registro = Column(DateTime)
    Fecha_actualizacion = Column(DateTime)
