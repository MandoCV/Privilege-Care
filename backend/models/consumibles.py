from sqlalchemy import Column, Integer, String, Text, Enum, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class EstatusEnum(enum.Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"
    En_Revision = "En Revisión"

class Consumible(Base):
    __tablename__ = "tbc_consumibles"

    ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Nombre = Column(String(255), nullable=False)
    Descripcion = Column(Text, nullable=True)
    Cantidad = Column(Integer, nullable=False)
    Tipo = Column(String(50), nullable=False)
    Departamento_ID = Column(Integer, nullable=False)
    Estatus = Column(Enum(EstatusEnum), nullable=False, default=EstatusEnum.Activo)
    Fecha_Registro = Column(TIMESTAMP, nullable=True, default="CURRENT_TIMESTAMP")
    Fecha_Actualizacion = Column(TIMESTAMP, nullable=True, default="CURRENT_TIMESTAMP", onupdate="CURRENT_TIMESTAMP")
    Observaciones = Column(Text, nullable=True)
    Espacio_Medico = Column(String(50), nullable=False)
