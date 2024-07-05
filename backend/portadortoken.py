from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from jwt_config import valida_token

class Portador(HTTPBearer):
    async def __call__(self,request:Request):
        autorizacion = await super().__call__(request)
        dato=valida_token(autorizacion.credentials)
        if dato['usuario']!= 'rlunas':
            raise HTTPException(status_code=403, detail ='No autorizado')
