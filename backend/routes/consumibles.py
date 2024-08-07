from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import crud.consumibles, config.db, schemas.consumibles, models.consumibles
from portadortoken import Portador

consumible = APIRouter()

models.consumibles.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@consumible.get("/consumibles/", response_model=List[schemas.consumibles.Consumible], tags=["Consumibles"], dependencies=[Depends(Portador())])
def read_consumibles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_consumibles = crud.consumibles.get_consumibles(db=db, skip=skip, limit=limit)
    return db_consumibles

@consumible.get("/consumible/{id}", response_model=schemas.consumibles.Consumible, tags=["Consumibles"], dependencies=[Depends(Portador())])
def read_consumible(id: int, db: Session = Depends(get_db)):
    db_consumible = crud.consumibles.get_consumible(db=db, id=id)
    if db_consumible is None:
        raise HTTPException(status_code=404, detail="Consumible not found")
    return db_consumible

@consumible.post("/consumibles/", response_model=schemas.consumibles.Consumible, tags=["Consumibles"])
def create_consumible(consumible: schemas.consumibles.ConsumibleCreate, db: Session = Depends(get_db)):
    db_consumible = crud.consumibles.get_consumible_by_nombre(db, nombre=consumible.Nombre)
    if db_consumible:
        raise HTTPException(status_code=400, detail="Consumible existente intenta nuevamente")
    return crud.consumibles.create_consumible(db=db, consumible=consumible)

@consumible.put("/consumible/{id}", response_model=schemas.consumibles.Consumible, tags=["Consumibles"], dependencies=[Depends(Portador())])
def update_consumible(id: int, consumible: schemas.consumibles.ConsumibleUpdate, db: Session = Depends(get_db)):
    db_consumible = crud.consumibles.update_consumible(db=db, id=id, consumible=consumible)
    if db_consumible is None:
        raise HTTPException(status_code=404, detail="Consumible no existe, no actualizado")
    return db_consumible

@consumible.delete("/consumible/{id}", response_model=schemas.consumibles.Consumible, tags=["Consumibles"], dependencies=[Depends(Portador())])
def delete_consumible(id: int, db: Session = Depends(get_db)):
    db_consumible = crud.consumibles.delete_consumible(db=db, id=id)
    if db_consumible is None:
        raise HTTPException(status_code=404, detail="Consumible no existe, no se pudo eliminar")
    return db_consumible
