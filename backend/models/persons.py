from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True)
    Titulo_Cortesia = Column(String(255))
    Nombre = Column(String(255))
    Primer_Apellido = Column(String(255))
    Segundo_Apellido = Column(String(255))
    Fecha_Nacimiento = Column(DateTime)
    Fotografia = Column(LONGTEXT)
    Genero = Column(String(255))
    Tipo_Sangre = Column(String(255))
    Estatus = Column(Boolean, default=False)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    #items = relationship("Item", back_populates="owner")
