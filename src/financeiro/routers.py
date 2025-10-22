"""
Rotas do domínio Financeiro (CNAB, Pagamentos)
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
async def ping():
    """Endpoint de teste"""
    return {"msg": "pong financeiro"}
EOF

echo "✅ Routers dos domínios criados"