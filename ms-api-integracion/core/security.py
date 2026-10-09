from fastapi import HTTPException, Header
import jwt
from jwt import InvalidTokenError
from core.config import settings

async def validar_token(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token no proporcionado")
    token = authorization.replace("Bearer ", "")
    try:
        return jwt.decode(token, settings.jwt_secret, algorithms=["HS256"])
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
