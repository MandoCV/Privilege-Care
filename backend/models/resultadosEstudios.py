from sqlalchemy import (Column,Integer,String,Text,Enum,DateTime,ForeignKey)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.db import Base
import models.estudios
#import models.pacientes, models.personal_medico

class ResultadosEstudios(Base):
    __tablename__ = "tbd_resultados_estudios"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    # Paciente_ID = Column(Integer, ForeignKey("tbb_pacientes.Persona_ID"), nullable=False)
    # Personal_Medico_ID = Column(Integer, ForeignKey("tbb_personal_medico.Persona_ID"), nullable=False)
    # Estudio_ID = Column(Integer, ForeignKey("tbc_estudios.ID"), nullable=False)
    Folio = Column(String(50), nullable=False, unique=True)
    Resultados = Column(Text, nullable=False)
    Observaciones = Column(Text, nullable=False)
    Estatus = Column(Enum(
        'Pendiente',
        'En Proceso',
        'Completado',
        'Aprobado',
        'Rechazado'
    ), nullable=True)
    Fecha_Registro = Column(DateTime, nullable=False, default=func.now())
    Fecha_Actualizacion = Column(DateTime, nullable=True, onupdate=func.now())

    # Relaciones
    estudio = relationship("Estudios", back_populates="resultados")
    # paciente = relationship("Pacientes", back_populates="resultados")
    # personal_medico = relationship("PersonalMedico", back_populates="resultados")

