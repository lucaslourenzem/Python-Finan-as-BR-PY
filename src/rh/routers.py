
"""
Rotas do domínio RH (Folha de pagamento)
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
async def ping():
    """Endpoint de teste"""
    return {"msg": "pong rh"}


