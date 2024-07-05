from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    usuario: str
    password: str
    created_at: datetime
    estatus: bool
    Id_persona: int

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int
    #owner_id: int clave foranea
    class Config:
        orm_mode = True
        
class UserLogin(BaseModel):
    usuario: str
    password: str


