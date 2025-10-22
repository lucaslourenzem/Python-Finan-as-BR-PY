from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.fiscal.router import router as fiscal_router
from src.rh.router import router as rh_router
from src.compliance.router import router as compliance_router
from src.financeiro.router import router as financeiro_router
from src.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION,
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Incluir routers dos domínios
app.include_router(fiscal_router, prefix="/api/v1")
app.include_router(rh_router, prefix="/api/v1")
app.include_router(compliance_router, prefix="/api/v1")
app.include_router(financeiro_router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
