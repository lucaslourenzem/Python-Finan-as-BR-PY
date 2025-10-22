FROM python:3.11-slim

# Variáveis de build
ARG APP_HOME=/app
WORKDIR ${APP_HOME}

# Dependências do sistema para pynfe e xmlsec
RUN apt-get update && apt-get install -y \
    libxml2-dev \
    libxmlsec1-dev \
    libxmlsec1-openssl \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY src/ ./src/
COPY alembic/ ./alembic/
COPY alembic.ini .

# Criar usuário não-root
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser ${APP_HOME}
USER appuser

# Expor porta
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=40s \
  CMD python -c "import requests; requests.get('http://localhost:8000/health')"

# Comando para iniciar
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]