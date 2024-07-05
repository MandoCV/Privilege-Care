import models.persons
import schemas.persons
from sqlalchemy.orm import Session
import models, schemas

def get_person(db: Session, id: int):
    return db.query(models.persons.Person).filter(models.persons.Person.id == id).first()

def get_person_by_nombre(db: Session, person: str):
    return db.query(models.persons.Person).filter(models.persons.Person.Nombre == person).first()

def get_persons(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.persons.Person).offset(skip).limit(limit).all()

def create_person(db: Session, person: schemas.persons.PersonCreate):
    db_person = models.persons.Person(Titulo_Cortesia=person.Titulo_Cortesia, Nombre=person.Nombre, Primer_Apellido=person.Primer_Apellido, Segundo_Apellido=person.Segundo_Apellido, Fecha_Nacimiento=person.Fecha_Nacimiento, Fotografia=person.Fotografia, Genero=person.Genero, Tipo_Sangre=person.Tipo_Sangre, Estatus=person.Estatus, Fecha_Registro=person.Fecha_Registro, Fecha_Actualizacion=person.Fecha_Actualizacion)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

def update_person(db: Session, id: int, person: schemas.persons.PersonUpdate):
    db_person = db.query(models.persons.Person).filter(models.persons.Person.id == id).first()
    if db_person:
        for var, value in vars(person).items():
            setattr(db_person, var, value) if value else None
        db.commit()
        db.refresh(db_person)
    return db_person

def delete_person(db: Session, id: int):
    db_person = db.query(models.persons.Person).filter(models.persons.Person.id == id).first()
    if db_person:
        db.delete(db_person)
        db.commit()
    return db_person