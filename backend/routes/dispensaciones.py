from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from portadortoken import Portador  # Asegúrate de ajustar esta importación según tu proyecto
import crud.dispensaciones, config.db, schemas.dispensaciones, models.dispensaciones
from typing import List

dispensacion = APIRouter()

models.dispensaciones.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@dispensacion.get("/dispensaciones/", response_model=List[schemas.dispensaciones.Dispensacion], tags=["Dispensaciones"], dependencies=[Depends(Portador())])
def read_dispensaciones(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_dispensaciones = crud.dispensaciones.get_dispensaciones(db=db, skip=skip, limit=limit)
    return db_dispensaciones

@dispensacion.get("/dispensacion/{ID}", response_model=schemas.dispensaciones.Dispensacion, tags=["Dispensaciones"], dependencies=[Depends(Portador())])
def read_dispensacion(ID: int, db: Session = Depends(get_db)):
    db_dispensacion = crud.dispensaciones.get_dispensacion(db=db, ID=ID)
    if db_dispensacion is None:
        raise HTTPException(status_code=404, detail="Dispensación no encontrada")
    return db_dispensacion

@dispensacion.post("/dispensaciones/", response_model=schemas.dispensaciones.Dispensacion, tags=["Dispensaciones"])
def create_dispensacion(dispensacion: schemas.dispensaciones.DispensacionCreate, db: Session = Depends(get_db)):
    return crud.dispensaciones.create_dispensacion(db=db, dispensacion=dispensacion)

@dispensacion.put("/dispensacion/{ID}", response_model=schemas.dispensaciones.Dispensacion, tags=["Dispensaciones"], dependencies=[Depends(Portador())])
def update_dispensacion(ID: int, dispensacion: schemas.dispensaciones.DispensacionUpdate, db: Session = Depends(get_db)):
    db_dispensacion = crud.dispensaciones.update_dispensacion(db=db, ID=ID, dispensacion=dispensacion)
    if db_dispensacion is None:
        raise HTTPException(status_code=404, detail="Dispensación no existente, no se actualizó")
    return db_dispensacion

@dispensacion.delete("/dispensacion/{ID}", response_model=schemas.dispensaciones.Dispensacion, tags=["Dispensaciones"], dependencies=[Depends(Portador())])
def delete_dispensacion(ID: int, db: Session = Depends(get_db)):
    db_dispensacion = crud.dispensaciones.delete_dispensacion(db=db, ID=ID)
    if db_dispensacion is None:
        raise HTTPException(status_code=404, detail="Dispensación no existe, no se pudo eliminar")
    return db_dispensacion
