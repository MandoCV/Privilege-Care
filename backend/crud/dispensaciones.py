import models.dispensaciones
import schemas.dispensaciones
from sqlalchemy.orm import Session

def get_dispensacion(db: Session, ID: int):
    return db.query(models.dispensaciones.Dispensacion).filter(models.dispensaciones.Dispensacion.ID == ID).first()

def get_dispensaciones(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.dispensaciones.Dispensacion).offset(skip).limit(limit).all()

def create_dispensacion(db: Session, dispensacion: schemas.dispensaciones.DispensacionCreate):
    db_dispensacion = models.dispensaciones.Dispensacion(
        RecetaMedica_id=dispensacion.RecetaMedica_id,
        PersonalMedico_id=dispensacion.PersonalMedico_id,
        Solicitud_id=dispensacion.Solicitud_id,
        Estatus=dispensacion.Estatus,
        Tipo=dispensacion.Tipo,
        TotalMedicamentosEntregados=dispensacion.TotalMedicamentosEntregados,
        Total_costo=dispensacion.Total_costo,
        Fecha_registro=dispensacion.Fecha_registro,
        Fecha_actualizacion=dispensacion.Fecha_actualizacion
    )
    db.add(db_dispensacion)
    db.commit()
    db.refresh(db_dispensacion)
    return db_dispensacion

def update_dispensacion(db: Session, ID: int, dispensacion: schemas.dispensaciones.DispensacionUpdate):
    db_dispensacion = db.query(models.dispensaciones.Dispensacion).filter(models.dispensaciones.Dispensacion.ID == ID).first()
    if db_dispensacion:
        for var, value in vars(dispensacion).items():
            setattr(db_dispensacion, var, value) if value is not None else None
        db.commit()
        db.refresh(db_dispensacion)
    return db_dispensacion

def delete_dispensacion(db: Session, ID: int):
    db_dispensacion = db.query(models.dispensaciones.Dispensacion).filter(models.dispensaciones.Dispensacion.ID == ID).first()
    if db_dispensacion:
        db.delete(db_dispensacion)
        db.commit()
    return db_dispensacion
