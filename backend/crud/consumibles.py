from sqlalchemy.orm import Session
import models.consumibles as models
import schemas.consumibles as schemas

def get_consumible(db: Session, id: int):
    return db.query(models.Consumible).filter(models.Consumible.ID == id).first()

def get_consumible_by_nombre(db: Session, nombre: str):
    return db.query(models.Consumible).filter(models.Consumible.Nombre == nombre).first()

def get_consumibles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Consumible).offset(skip).limit(limit).all()

def create_consumible(db: Session, consumible: schemas.ConsumibleCreate):
    db_consumible = models.Consumible(
        Nombre=consumible.Nombre,
        Descripcion=consumible.Descripcion,
        Cantidad=consumible.Cantidad,
        Tipo=consumible.Tipo,
        Departamento_ID=consumible.Departamento_ID,
        Estatus=consumible.Estatus,
        Observaciones=consumible.Observaciones,
        Espacio_Medico=consumible.Espacio_Medico
    )
    db.add(db_consumible)
    db.commit()
    db.refresh(db_consumible)
    return db_consumible

def update_consumible(db: Session, id: int, consumible: schemas.ConsumibleUpdate):
    db_consumible = db.query(models.Consumible).filter(models.Consumible.ID == id).first()
    if db_consumible:
        for var, value in vars(consumible).items():
            setattr(db_consumible, var, value) if value else None
        db.commit()
        db.refresh(db_consumible)
    return db_consumible

def delete_consumible(db: Session, id: int):
    db_consumible = db.query(models.Consumible).filter(models.Consumible.ID == id).first()
    if db_consumible:
        db.delete(db_consumible)
        db.commit()
    return db_consumible
