from fastapi import APIRouter, Depends
from core.config import settings
from core.security import validar_token
from clients.base import get_json

router = APIRouter(prefix="/api/tareas", tags=["Tareas"])

@router.get("/{estudiante_id}")
async def listar_tareas(estudiante_id: int, usuario=Depends(validar_token)):
    return await get_json(settings.tareas_url, f"/tareas/estudiante/{estudiante_id}")
