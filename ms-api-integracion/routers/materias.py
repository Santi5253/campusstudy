from fastapi import APIRouter, Depends
from core.config import settings
from core.security import validar_token
from clients.base import get_json

router = APIRouter(prefix="/api/materias", tags=["Materias"])

@router.get("")
async def listar_materias(usuario=Depends(validar_token)):
    return await get_json(settings.materias_url, "/materias")
