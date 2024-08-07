from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from portadortoken import Portador  # Asegúrate de ajustar esta importación según tu proyecto
import crud.medicamentos, config.db, schemas.medicamentos, models.medicamentos
from typing import List

medicamento = APIRouter()

models.medicamentos.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@medicamento.get("/medicamentos/", response_model=List[schemas.medicamentos.Medicamento], tags=["Medicamentos"], dependencies=[Depends(Portador())])
def read_medicamentos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_medicamentos = crud.medicamentos.get_medicamentos(db=db, skip=skip, limit=limit)
    return db_medicamentos

@medicamento.get("/medicamento/{ID}", response_model=schemas.medicamentos.Medicamento, tags=["Medicamentos"], dependencies=[Depends(Portador())])
def read_medicamento(ID: int, db: Session = Depends(get_db)):
    db_medicamento = crud.medicamentos.get_medicamento(db=db, ID=ID)
    if db_medicamento is None:
        raise HTTPException(status_code=404, detail="Medicamento no encontrado")
    return db_medicamento

@medicamento.post("/medicamentos/", response_model=schemas.medicamentos.Medicamento, tags=["Medicamentos"])
def create_medicamento(medicamento: schemas.medicamentos.MedicamentoCreate, db: Session = Depends(get_db)):
    db_medicamento = crud.medicamentos.get_medicamentos_by_nombre(db, Nombre_comercial=medicamento.Nombre_comercial)
    if db_medicamento:
        raise HTTPException(status_code=400, detail="Medicamento existente, intenta nuevamente")
    return crud.medicamentos.create_medicamento(db=db, medicamento=medicamento)

@medicamento.put("/medicamento/{ID}", response_model=schemas.medicamentos.Medicamento, tags=["Medicamentos"], dependencies=[Depends(Portador())])
def update_medicamento(ID: int, medicamento: schemas.medicamentos.MedicamentoUpdate, db: Session = Depends(get_db)):
    db_medicamento = crud.medicamentos.update_medicamento(db=db, ID=ID, medicamento=medicamento)
    if db_medicamento is None:
        raise HTTPException(status_code=404, detail="Medicamento no existente, no se actualizó")
    return db_medicamento

@medicamento.delete("/medicamento/{ID}", response_model=schemas.medicamentos.Medicamento, tags=["Medicamentos"], dependencies=[Depends(Portador())])
def delete_medicamento(ID: int, db: Session = Depends(get_db)):
    db_medicamento = crud.medicamentos.delete_medicamento(db=db, ID=ID)
    if db_medicamento is None:
        raise HTTPException(status_code=404, detail="Medicamento no existe, no se pudo eliminar")
    return db_medicamento
