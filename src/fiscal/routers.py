"""
Rotas do domínio Fiscal (NFS-e, NFC-e, etc)
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
async def ping():
    """Endpoint de teste"""
    return {"msg": "pong fiscal"}

@router.get("/")
async def listar_notas():
    """Lista notas fiscais (placeholder)"""
    return {"notas": [], "total": 0}
