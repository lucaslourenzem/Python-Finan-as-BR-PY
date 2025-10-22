"""
Rotas do domínio Compliance (Verificações fiscais)
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
async def ping():
    """Endpoint de teste"""
    return {"msg": "pong compliance"}


