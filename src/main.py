"""
Arquivo principal da aplicação FastAPI
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Imports corrigidos: routers.py (não router.py)
from src.fiscal.routers import router as fiscal_router
from src.rh.routers import router as rh_router
from src.compliance.routers import router as compliance_router
from src.financeiro.routers import router as financeiro_router
from src.core.config import settings

# Criar aplicação FastAPI
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION,
    description="API para automação financeira e fiscal brasileira",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Incluir routers dos domínios
app.include_router(fiscal_router, prefix="/api/v1/fiscal", tags=["Fiscal"])
app.include_router(rh_router, prefix="/api/v1/rh", tags=["RH"])
app.include_router(compliance_router, prefix="/api/v1/compliance", tags=["Compliance"])
app.include_router(financeiro_router, prefix="/api/v1/financeiro", tags=["Financeiro"])

@app.get("/", tags=["Root"])
async def root():
    """Endpoint raiz"""
    return {
        "message": "Financial API",
        "version": settings.API_VERSION,
        "docs": "/api/docs"
    }

@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": settings.API_VERSION
    }
