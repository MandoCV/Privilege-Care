import models.lotes
import schemas.lotes
from sqlalchemy.orm import Session

def get_lote(db: Session, id: int):
    return db.query(models.lotes.Lote).filter(models.lotes.Lote.ID == id).first()

def get_lotes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.lotes.Lote).offset(skip).limit(limit).all()

def create_lote(db: Session, lote: schemas.lotes.LoteCreate):
    db_lote = models.lotes.Lote(
        Medicamento_ID=lote.Medicamento_ID,
        Personal_Medico_ID=lote.Personal_Medico_ID,
        Clave=lote.Clave,
        Estatus=lote.Estatus,
        Costo_Total=lote.Costo_Total,
        Cantidad=lote.Cantidad,
        Ubicacion=lote.Ubicacion,
        Fecha_Registro=lote.Fecha_Registro,
        Fecha_Actualizacion=lote.Fecha_Actualizacion
    )
    db.add(db_lote)
    db.commit()
    db.refresh(db_lote)
    return db_lote

def update_lote(db: Session, id: int, lote: schemas.lotes.LoteUpdate):
    db_lote = db.query(models.lotes.Lote).filter(models.lotes.Lote.ID == id).first()
    if db_lote:
        for var, value in vars(lote).items():
            setattr(db_lote, var, value) if value is not None else None
        db.commit()
        db.refresh(db_lote)
    return db_lote

def delete_lote(db: Session, id: int):
    db_lote = db.query(models.lotes.Lote).filter(models.lotes.Lote.ID == id).first()
    if db_lote:
        db.delete(db_lote)
        db.commit()
    return db_lote
