from fastapi import APIRouter,HTTPException,Depends,Request
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from portadortoken import Portador
import crud.lotes, config.db, schemas.lotes, models.lotes
from typing import List

lote = APIRouter()

models.lotes.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@lote.get("/lotes/", response_model=List[schemas.lotes.Lote], tags=["Lotes"],dependencies=[Depends(Portador())])
def read_lotes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_lotes = crud.lotes.get_lotes(db=db, skip=skip, limit=limit)
    return db_lotes

@lote.get("/lote/{id}", response_model=schemas.lotes.Lote, tags=["Lotes"],dependencies=[Depends(Portador())])
def read_lote(id: int, db: Session = Depends(get_db)):
    db_lote = crud.lotes.get_lote(db=db, id=id)
    if db_lote is None:
        raise HTTPException(status_code=404, detail="Lote no encontrado")
    return db_lote

@lote.post("/lotes/", response_model=schemas.lotes.Lote, tags=["Lotes"])
def create_lote(lote: schemas.lotes.LoteCreate, db: Session = Depends(get_db)):
    return crud.lotes.create_lote(db=db, lote=lote)

@lote.put("/lote/{id}", response_model=schemas.lotes.Lote, tags=["Lotes"],dependencies=[Depends(Portador())])
def update_lote(id: int, lote: schemas.lotes.LoteUpdate, db: Session = Depends(get_db)):
    db_lote = crud.lotes.update_lote(db=db, id=id, lote=lote)
    if db_lote is None:
        raise HTTPException(status_code=404, detail="Lote no encontrado o no actualizado")
    return db_lote

@lote.delete("/lote/{id}", response_model=schemas.lotes.Lote, tags=["Lotes"],dependencies=[Depends(Portador())])
def delete_lote(id: int, db: Session = Depends(get_db)):
    db_lote = crud.lotes.delete_lote(db=db, id=id)
    if db_lote is None:
        raise HTTPException(status_code=404, detail="Lote no encontrado o no eliminado")
    return db_lote
