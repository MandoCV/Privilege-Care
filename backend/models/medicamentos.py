from sqlalchemy import Column, Integer, String, Enum, DateTime, Boolean
from sqlalchemy.dialects.mysql import DECIMAL
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class ViaAdministracion(enum.Enum):
    Oral = "Oral"
    Intravenoso = "Intravenoso"
    Rectal = "Rectal"
    Cutáneo = "Cutáneo"
    Subcutáneo = "Subcutáneo"
    Oftálmica = "Oftálmica"
    Ótica = "Ótica"
    Nasal = "Nasal"
    Tópica = "Tópica"
    Parenteral = "Parenteral"

class Presentacion(enum.Enum):
    Comprimidos = "Comprimidos"
    Grageas = "Grageas"
    Cápsulas = "Cápsulas"
    Jarabes = "Jarabes"
    Gotas = "Gotas"
    Solución = "Solución"
    Pomada = "Pomada"
    Jabón = "Jabón"
    Supositorios = "Supositorios"
    Viales = "Viales"

class Tipo(enum.Enum):
    Analgésicos = "Analgésicos"
    Antibióticos = "Antibióticos"
    Antidepresivos = "Antidepresivos"
    Antihistamínicos = "Antihistamínicos"
    Antiinflamatorios = "Antiinflamatorios"
    Antipsicóticos = "Antipsicóticos"

class Medicamento(Base):
    __tablename__ = "tbc_medicamentos"
    
    ID = Column(Integer, primary_key=True, index=True)
    Nombre_comercial = Column(String(80))
    Nombre_generico = Column(String(80))
    Via_administracion = Column(Enum(ViaAdministracion))
    Presentacion = Column(Enum(Presentacion))
    Tipo = Column(Enum(Tipo))
    Cantidad = Column(DECIMAL(10, 2))
    Volumen = Column(DECIMAL(10, 2), nullable=True)
    Estatus = Column(Boolean, default=False)
    Fecha_registro = Column(DateTime)
    Fecha_actualizacion = Column(DateTime)
