import models.medicamentos
import schemas.medicamentos
from sqlalchemy.orm import Session

def get_medicamento(db: Session, ID: int):
    return db.query(models.medicamentos.Medicamento).filter(models.medicamentos.Medicamento.ID == ID).first()

def get_medicamentos_by_nombre(db: Session, Nombre_comercial: str):
    return db.query(models.medicamentos.Medicamento).filter(models.medicamentos.Medicamento.Nombre_comercial == Nombre_comercial).first()

def get_medicamentos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.medicamentos.Medicamento).offset(skip).limit(limit).all()

def create_medicamento(db: Session, medicamento: schemas.medicamentos.MedicamentoCreate):
    db_medicamento = models.medicamentos.Medicamento(
        Nombre_comercial=medicamento.Nombre_comercial,
        Nombre_generico=medicamento.Nombre_generico,
        Via_administracion=medicamento.Via_administracion,
        Presentacion=medicamento.Presentacion,
        Tipo=medicamento.Tipo,
        Cantidad=medicamento.Cantidad,
        Volumen=medicamento.Volumen,
        Estatus=medicamento.Estatus,
        Fecha_registro=medicamento.Fecha_registro,
        Fecha_actualizacion=medicamento.Fecha_actualizacion
    )
    db.add(db_medicamento)
    db.commit()
    db.refresh(db_medicamento)
    return db_medicamento

def update_medicamento(db: Session, ID: int, medicamento: schemas.medicamentos.MedicamentoUpdate):
    db_medicamento = db.query(models.medicamentos.Medicamento).filter(models.medicamentos.Medicamento.ID == ID).first()
    if db_medicamento:
        for var, value in vars(medicamento).items():
            setattr(db_medicamento, var, value) if value is not None else None
        db.commit()
        db.refresh(db_medicamento)
    return db_medicamento

def delete_medicamento(db: Session, ID: int):
    db_medicamento = db.query(models.medicamentos.Medicamento).filter(models.medicamentos.Medicamento.ID == ID).first()
    if db_medicamento:
        db.delete(db_medicamento)
        db.commit()
    return db_medicamento
