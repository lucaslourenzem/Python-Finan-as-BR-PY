
# 💰 Financial API - Sistema Financeiro Brasileiro

API REST para automação de processos financeiros e fiscais no Brasil.

## 🚀 Tecnologias

- Python 3.11+
- FastAPI 0.115+
- PostgreSQL 16+
- Redis 7+
- Docker & Docker Compose

## 📋 Domínios

- **Fiscal**: Emissão de NFS-e, NFC-e
- **RH**: Cálculos de folha de pagamento
- **Compliance**: Verificação de pendências fiscais
- **Financeiro**: CNAB, pagamentos bancários

## 🔧 Instalação

### 1. Clonar repositório
```bash
git clone <seu-repo>
cd <nome-projeto>
```

### 2. Criar ambiente virtual
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Instalar python-cnab via Git
```bash
pip install git+https://github.com/scardine/cnab.git
```

### 5. Configurar variáveis de ambiente
```bash
cp .env.example .env
# Edite .env com suas configurações
```

### 6. Rodar servidor
```bash
uvicorn src.main:app --reload --port 8000
```

## 📖 Documentação

- Swagger UI: http://localhost:8000/api/docs
- ReDoc: http://localhost:8000/api/redoc

## 🧪 Testes
```bash
# Rodar todos os testes
pytest

# Com coverage
pytest --cov=src --cov-report=html

# Ver relatório
open htmlcov/index.html
```

## 🐳 Docker
```bash
# Subir todos os serviços
docker-compose up -d

# Ver logs
docker-compose logs -f api

# Parar serviços
docker-compose down
```

## 📁 Estrutura
```
src/
├── fiscal/        # Domínio fiscal (NFS-e)
├── rh/            # Domínio RH (folha)
├── compliance/    # Domínio compliance
├── financeiro/    # Domínio financeiro (CNAB)
└── core/          # Código compartilhado
```

## ⚙️ Configuração

Edite `.env` com:
- Credenciais de banco de dados
- Tokens de APIs (Focus NFe, etc)
- Certificados digitais
- Configurações CNAB

## 🔒 Segurança

⚠️ **NUNCA** versione:
- Arquivo `.env` com secrets reais
- Certificados digitais (`.pfx`, `.pem`)
- Chaves privadas
- Credenciais de produção

## 📝 Status do Projeto

- [x] Configuração inicial
- [ ] Módulo Fiscal (NFS-e)
- [ ] Módulo RH (Folha)
- [ ] Módulo Compliance
- [ ] Módulo Financeiro (CNAB)
- [ ] Testes completos
- [ ] Deploy

## 📄 Licença

MIT
