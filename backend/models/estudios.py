from sqlalchemy import (Column,Integer,String,ForeignKey,Text,DateTime,DECIMAL)
from sqlalchemy.orm import relationship
from config.db import Base
# import models.solicitudes, models.consumibles

class Estudios(Base):
    __tablename__ = "tbc_estudios"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Tipo = Column(String(50), nullable=False)
    Nivel_Urgencia = Column(String(50), nullable=False)
    Solicitud_ID = Column(Integer, ForeignKey("tbd_solicitudes.ID"), nullable=False)
    Consumibles_ID = Column(Integer, ForeignKey("tbc_consumibles.id"), nullable=True)
    Estatus = Column(String(50), nullable=False)
    Total_Costo = Column(DECIMAL(10, 2), nullable=False)
    Dirigido_A = Column(String(100), nullable=True)
    Observaciones = Column(Text, nullable=True)
    Fecha_Registro = Column(DateTime, nullable=False)
    Fecha_Actualizacion = Column(DateTime, nullable=True)

    # Relaciones
    # solicitud = relationship("Solicitudes", back_populates="estudios")
    # consumible = relationship("Consumibles", back_populates="estudios")

