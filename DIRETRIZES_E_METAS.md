# 📋 Python Finanças BR-PY - Diretrizes e Metas de Estudo

**Versão:** 1.0  
**Data de Criação:** Outubro 2025  
**Dedicação Recomendada:** 10-15h/semana  
**Duração Total:** 12 semanas (3 meses)

---

## 🎯 Visão Geral do Projeto

Este é um **plano de aprendizado prático estruturado** para dominar Python aplicado a APIs financeiras, com foco na automação de processos fiscais, contábeis e bancários nos contextos brasileiro e paraguaio.

### Objetivo Principal
Desenvolver uma **API modular REST em Python** que automatize:
- ✅ Emissão de Notas Fiscais de Serviço (NFS-e)
- ✅ Cálculo de folha de pagamento (RH)
- ✅ Verificação de pendências fiscais
- ✅ Integração e automação de pagamentos bancários

### Resultado Final Esperado
Um **protótipo de produto** (não apenas educacional) com:
- Sistema modularizado com 4 domínios independentes (Fiscal, RH, Compliance, Financeiro)
- API REST funcional com autenticação e documentação
- Suporte inicial para Brasil com extensão preparada para Paraguai
- Testes unitários e integração
- Fluxos de negócio completos testados

---

## 📊 Perfil do Aprendiz

| Aspecto | Detalhe |
|--------|--------|
| **Nível Atual** | Intermediário em Python, Django/REST, pouco Flask |
| **Consideração para Estudo** | **Iniciante** (para aprender profundamente) |
| **IDE** | VSCode (preferência do usuário) |
| **Ferramentas** | Python 3.10+, venv, Git, APIs REST |
| **Modelagem** | Do zero (cálculos, formatos) → Integração com APIs reais |

---

## 🗓️ Cronograma Detalhado de 12 Semanas

### **FASE 1: FUNDAMENTOS (Semanas 1-2)**

#### Semana 1: Revisão de APIs e Frameworks
**Tempo Estimado:** 8-10 horas

**Objetivos:**
- [ ] Revisar HTTP, JSON, requisições GET/POST
- [ ] Comparar Flask vs FastAPI vs Django REST
- [ ] Escolher framework (recomendação: **FastAPI** para performance + documentação)
- [ ] Configurar ambiente (venv, VSCode, extensões Python)
- [ ] Criar repositório Git local ou GitHub privado

**Entregas:**
- Projeto Hello World em FastAPI com 3 endpoints dummy
- Arquivo `requirements.txt` com dependências básicas
- Primeiro commit no Git

**Recursos:**
- Documentação: [FastAPI](https://fastapi.tiangolo.com/) ou [Flask](https://flask.palletsprojects.com/)
- Exemplo simples: GET `/health`, POST `/echo`, GET `/docs` (Swagger automático)

**Checkpoint:** 
```bash
# Comando de teste
curl http://localhost:8000/health
# Resposta esperada: {"status": "ok"}
```

---

#### Semana 2: Estrutura Base da API
**Tempo Estimado:** 8-10 horas

**Objetivos:**
- [ ] Design da arquitetura modular (4 domínios)
- [ ] Criar estrutura de pastas do projeto
- [ ] Implementar roteamento inicial (v1)
- [ ] Escrever testes unitários básicos (TDD)
- [ ] Documentar endpoints com Swagger/OpenAPI

**Estrutura de Pastas:**
```
Python-Financas-BR-PY/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Entrada da aplicação
│   ├── config.py               # Configurações
│   ├── fiscal/                 # Domínio: NFS-e, NFTS
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── services.py
│   │   └── routes.py
│   ├── rh/                     # Domínio: Folha de Pagamento
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── services.py
│   │   └── routes.py
│   ├── compliance/             # Domínio: Pendências Fiscais
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── services.py
│   │   └── routes.py
│   ├── financeiro/             # Domínio: Pagamentos
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── services.py
│   │   └── routes.py
│   └── utils/                  # Funções compartilhadas
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── test_fiscal.py
│   ├── test_rh.py
│   ├── test_compliance.py
│   └── test_financeiro.py
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

**Entregas:**
- Estrutura completa de pastas criada
- 4 endpoints dummy (um por domínio): `/fiscal/`, `/rh/`, `/compliance/`, `/financeiro/`
- Arquivo `main.py` com inicialização da API
- 3-5 testes unitários básicos
- Documentação Swagger acessível em `/docs`

**Checkpoint:**
```bash
# Verificar estrutura
tree -L 3 app/
# Rodar testes
pytest tests/
# Acessar documentação
# Abrir http://localhost:8000/docs
```

---

### **FASE 2: DOMÍNIO FISCAL (Semanas 3-5)**

#### Semana 3: Conceitos de NFS-e + Modelagem
**Tempo Estimado:** 10-12 horas

**Objetivos:**
- [ ] Estudar o que é NFS-e (requisitos municipais)
- [ ] Entender padrão ABRASF
- [ ] Pesquisar NFS-e em sua cidade/São Paulo
- [ ] Criar modelo de dados Python (classes/dataclasses)
- [ ] Gerar XML fictício (sem enviar a lugar nenhum)

**Conceitos-Chave:**
- NFS-e = Nota Fiscal Eletrônica de Serviço (documento fiscal municipal)
- Cada prefeitura pode ter sistema próprio ou usar padrão ABRASF
- Requer certificado digital em muitos casos
- Dados necessários: prestador (CNPJ, inscrição), tomador, serviço, ISS

**Entregas:**
```python
# Exemplo: models.py no módulo fiscal/
from dataclasses import dataclass
from typing import Optional

@dataclass
class Prestador:
    cnpj: str
    razao_social: str
    inscricao_municipal: str
    endereco: str

@dataclass
class Tomador:
    cpf_cnpj: str
    nome: str
    endereco: str

@dataclass
class Servico:
    descricao: str
    valor: float
    aliquota_iss: float  # em %
    
@dataclass
class NotaFiscalServico:
    prestador: Prestador
    tomador: Tomador
    servico: Servico
    numero: Optional[str] = None
    data_emissao: Optional[str] = None
```

- Função que gera XML da NFS-e (simplificado)
- Testes validando modelo
- Documentação descrevendo campos

**Checkpoint:**
```python
# Teste básico
nfs = NotaFiscalServico(...)
xml = gerar_xml_nfse(nfs)
print(xml)  # Deve imprimir XML estruturado
```

---

#### Semana 4: Integração com API de Terceiro
**Tempo Estimado:** 10-12 horas

**Objetivos:**
- [ ] Cadastrar-se em API unificada (ex: Focus NFe - oferece sandbox)
- [ ] Obter token de teste
- [ ] Implementar chamada POST para emitir NFS-e
- [ ] Tratar respostas (sucesso, erros)
- [ ] Consultar NFS-e recebidas

**Passos Práticos:**
1. Registrar em [Focus NFe](https://focusnfe.com.br/) (oferecem ambiente de homologação gratuito)
2. Gerar API key de teste
3. Implementar função em `fiscal/services.py`:

```python
import requests
from typing import Dict

def emitir_nfse_focus(nfs: NotaFiscalServico, api_key: str) -> Dict:
    """Emite NFS-e via Focus NFe"""
    url = "https://homolog.focusnfe.com.br/v2/nfse"
    
    payload = {
        "prestador": {
            "cnpj": nfs.prestador.cnpj,
            "inscricao_municipal": nfs.prestador.inscricao_municipal
        },
        "tomador": {
            "cpf_cnpj": nfs.tomador.cpf_cnpj,
            "nome": nfs.tomador.nome
        },
        "servico": {
            "descricao": nfs.servico.descricao,
            "valor_servicos": nfs.servico.valor,
            "aliquota": nfs.servico.aliquota_iss
        }
    }
    
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 201:
        return {"status": "success", "nfse_id": response.json()["id"]}
    else:
        return {"status": "error", "message": response.json()}
```

**Entregas:**
- Função testada emitindo NFS-e em homologação
- Tratamento de erros implementado
- Testes unitários para respostas de sucesso e erro
- Documentação de como obter API key

**Checkpoint:**
```python
# Teste com dados fictícios
resultado = emitir_nfse_focus(nfs_teste, api_key="seu_token")
assert resultado["status"] == "success"
```

---

#### Semana 5: Integração Web Service Direto + API REST
**Tempo Estimado:** 10-12 horas

**Objetivos:**
- [ ] Estudar SOAP/WSDL (alternativa a REST)
- [ ] Usar biblioteca `zeep` ou `suds` para consumir web service
- [ ] Implementar integração direta com prefeitura (São Paulo, p.ex.)
- [ ] Integrar tudo na API REST (endpoint POST `/api/v1/nfse/emitir`)
- [ ] Testes e validação

**Por que aprender SOAP?**
Muitas prefeituras ainda usam SOAP. Aprender ambos (REST + SOAP) é valioso.

**Implementação Prática:**

```python
# fiscal/services.py - Opção com biblioteca PyNFe
from pynfe.utils import mk_fileout
from pynfe.entidades import Cliente, PessoaFisica, Empresa

def emitir_nfse_direto(nfs: NotaFiscalServico, certificado_path: str):
    """Emite NFS-e diretamente para prefeitura (simplificado)"""
    # Nota: Implementação completa requer certificado digital
    # Este é um esboço conceitual
    try:
        # Montar objeto de NFS-e conforme padrão ABRASF
        # Assinar XML com certificado
        # Enviar para web service da prefeitura
        # Retornar protocolo
        pass
    except Exception as e:
        return {"status": "error", "message": str(e)}
```

```python
# fiscal/routes.py - Endpoint REST
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1/nfse", tags=["NFS-e"])

class NotaFiscalRequest(BaseModel):
    prestador_cnpj: str
    tomador_cpf_cnpj: str
    descricao_servico: str
    valor: float
    aliquota_iss: float

@router.post("/emitir")
async def emitir_nfse(nota: NotaFiscalRequest):
    """Emite uma NFS-e"""
    try:
        # Converter request para modelo interno
        nfs = NotaFiscalServico(...)
        
        # Tentar API de terceiro primeiro
        resultado = emitir_nfse_focus(nfs, api_key=...)
        
        if resultado["status"] == "success":
            return {"status": "ok", "nfse_id": resultado["nfse_id"]}
        else:
            raise HTTPException(status_code=500, detail=resultado["message"])
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/consultar/{numero}")
async def consultar_nfse(numero: str):
    """Consulta status de uma NFS-e emitida"""
    # Implementar lógica de consulta
    pass

@router.get("/recebidas")
async def listar_nfse_recebidas(cnpj: str):
    """Lista NFS-e recebidas por CNPJ"""
    # Implementar lógica
    pass
```

**Entregas:**
- 3 endpoints REST implementados (`/emitir`, `/consultar`, `/recebidas`)
- Tratamento de erros robusto
- Testes de integração
- Documentação Swagger clara

**Checkpoint - Testar via Swagger:**
```
POST /api/v1/nfse/emitir
Body: {
  "prestador_cnpj": "12.345.678/0001-90",
  "tomador_cpf_cnpj": "987.654.321-00",
  "descricao_servico": "Consultoria técnica",
  "valor": 1000.00,
  "aliquota_iss": 5.0
}

Response: {
  "status": "ok",
  "nfse_id": "123456"
}
```

---

### **FASE 3: DOMÍNIO RH (Semanas 6-7)**

#### Semana 6: Cálculos de Folha (Do Zero)
**Tempo Estimado:** 10-12 horas

**Objetivos:**
- [ ] Pesquisar tabelas atuais INSS 2024/2025
- [ ] Pesquisar tabelas IRRF 2024/2025
- [ ] Implementar funções puras de cálculo
- [ ] Testar contra calculadoras online
- [ ] Documentar cada fórmula

**Informações Necessárias (2025 - Atualizar conforme mudanças):**

**INSS (Contribuição Previdenciária):**
- Faixa 1: até R$ 1.412,00 → 7,5%
- Faixa 2: R$ 1.412,01 a R$ 2.666,68 → 9%
- Faixa 3: R$ 2.666,69 a R$ 4.000,03 → 12%
- Faixa 4: R$ 4.000,04 a R$ 7.786,02 → 14%
- Teto: R$ 1.088,00 (máximo a descontar)

**IRRF (Imposto de Renda Retido na Fonte):**
- Isento: até R$ 1.903,98
- Faixa 1: até 2.826,65 → 7,5% (dedução parcela: R$ 142,80)
- Faixa 2: até 3.751,05 → 15% (dedução parcela: R$ 354,80)
- Faixa 3: até 4.664,68 → 22,5% (dedução parcela: R$ 636,13)
- Faixa 4: acima → 27,5% (dedução parcela: R$ 869,36)

**FGTS:** 8% do salário bruto (pago pela empresa, não desconto)

**Entregas:**

```python
# rh/models.py
from dataclasses import dataclass
from enum import Enum

class TipoFuncionario(Enum):
    CLT = "clt"
    AUTONOMO = "autonomo"
    ESTAGIARIO = "estagiario"

@dataclass
class Funcionario:
    nome: str
    cpf: str
    salario_bruto: float
    dependentes: int = 0
    tipo: TipoFuncionario = TipoFuncionario.CLT

@dataclass
class FolhaPagamento:
    funcionario: Funcionario
    salario_bruto: float
    inss: float
    irrf: float
    fgts: float
    outros_descontos: float
    salario_liquido: float

# rh/services.py
def calcular_inss(salario_bruto: float) -> float:
    """Calcula INSS sobre salário bruto"""
    if salario_bruto <= 1412.00:
        return salario_bruto * 0.075
    elif salario_bruto <= 2666.68:
        return salario_bruto * 0.09
    elif salario_bruto <= 4000.03:
        return salario_bruto * 0.12
    elif salario_bruto <= 7786.02:
        return salario_bruto * 0.14
    else:
        return 1088.00  # Teto

def calcular_irrf(salario_bruto: float, inss: float, dependentes: int = 0) -> float:
    """Calcula IRRF"""
    base_calculo = salario_bruto - inss - (dependentes * 189.59)  # Dedução por dependente
    
    if base_calculo <= 1903.98:
        return 0.0
    elif base_calculo <= 2826.65:
        return base_calculo * 0.075 - 142.80
    elif base_calculo <= 3751.05:
        return base_calculo * 0.15 - 354.80
    elif base_calculo <= 4664.68:
        return base_calculo * 0.225 - 636.13
    else:
        return base_calculo * 0.275 - 869.36

def calcular_fgts(salario_bruto: float) -> float:
    """FGTS é 8% do bruto (não é desconto do funcionário)"""
    return salario_bruto * 0.08

def calcular_folha(funcionario: Funcionario) -> FolhaPagamento:
    """Calcula folha de pagamento completa"""
    inss = calcular_inss(funcionario.salario_bruto)
    irrf = calcular_irrf(funcionario.salario_bruto, inss, funcionario.dependentes)
    fgts = calcular_fgts(funcionario.salario_bruto)
    outros_descontos = 0.0  # Pode incluir vale transporte, plano saúde, etc.
    
    salario_liquido = (funcionario.salario_bruto - inss - irrf - outros_descontos)
    
    return FolhaPagamento(
        funcionario=funcionario,
        salario_bruto=funcionario.salario_bruto,
        inss=inss,
        irrf=irrf,
        fgts=fgts,
        outros_descontos=outros_descontos,
        salario_liquido=salario_liquido
    )
```

**Testes contra Calculadora Online:**
```python
# tests/test_rh.py
def test_calcular_inss():
    # Exemplo: Salário de R$ 2.000
    # Esperado: 2000 * 0.09 = R$ 180
    assert calcular_inss(2000.0) == 180.0

def test_calcular_irrf():
    # Exemplo: Salário de R$ 3.000, INSS de R$ 270
    # Base: 3000 - 270 = 2730
    # IRRF: 2730 * 0.075 - 142.80 = R$ 62.25
    assert calcular_irrf(3000.0, 270.0) == 62.25

def test_folha_completa():
    func = Funcionario("João Silva", "123.456.789-00", 3000.0, 0)
    folha = calcular_folha(func)
    assert folha.salario_liquido > 0
    assert folha.salario_liquido < 3000.0  # Desconto de algo
```

**Checkpoint:**
- Todos os testes passando ✅
- Resultados validados com calculadora online ✅
- Fórmulas documentadas ✅

---

#### Semana 7: Extensões RH + Integração API
**Tempo Estimado:** 10-12 horas

**Objetivos:**
- [ ] Implementar 13º salário e férias
- [ ] Implementar pagamentos a autônomos (RPA)
- [ ] Criar script que lê CSV de funcionários
- [ ] Gerar relatório de folha (tabular ou PDF simples)
- [ ] Integrar endpoints REST

**Extensões Implementar:**

```python
# rh/services.py - Extensões

def calcular_decimo_terceiro(salario_mensal: float, meses_trabalhados: int) -> float:
    """Calcula 13º salário proporcional"""
    return (salario_mensal / 12) * meses_trabalhados

def calcular_ferias(salario_mensal: float, dias_tirados: int = 30) -> float:
    """Calcula férias com 1/3 adicional"""
    valor_dias = (salario_mensal / 30) * dias_tirado
    return valor_dias * 1.333  # 1/3 adicional

def calcular_rpa_autonomo(valor_servico: float, iss_retencao: bool = True, 
                         inss_contribuinte: float = 0.11) -> Dict:
    """
    Calcula pagamento a autônomo (RPA - Recibo de Pagamento Autônomo)
    - ISS: 5% (opcional, depende da prefeitura)
    - INSS: 11% do autônomo (com teto)
    - IRRF: Conforme tabela (base diferente)
    """
    iss = valor_servico * 0.05 if iss_retencao else 0.0
    inss = valor_servico * inss_contribuinte  # Teto: R$ 856 (2025)
    irrf = calcular_irrf_autonomo(valor_servico - iss - inss)
    
    liquido = valor_servico - iss - inss - irrf
    
    return {
        "valor_servico": valor_servico,
        "iss": iss,
        "inss": inss,
        "irrf": irrf,
        "liquido": liquido
    }

def calcular_irrf_autonomo(valor_liquido: float) -> float:
    """IRRF para autônomos tem tabela diferente"""
    # Simplificado: 15% acima de R$ 1.903.98
    if valor_liquido <= 1903.98:
        return 0.0
    else:
        return valor_liquido * 0.15
```

**Rotas REST:**

```python
# rh/routes.py
from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1/rh", tags=["RH"])

class SalarioRequest(BaseModel):
    salario_bruto: float
    dependentes: int = 0
    horas_extras_50: float = 0.0
    horas_extras_100: float = 0.0
    outros_descontos: float = 0.0

@router.post("/salario")
async def calcular_salario(dados: SalarioRequest):
    """Calcula salário líquido"""
    # Implementar lógica
    pass

@router.post("/folha")
async def calcular_folha_mensal(funcionarios: list[SalarioRequest]):
    """Calcula folha de pagamento para múltiplos funcionários"""
    # Implementar lógica
    pass

@router.post("/rpa")
async def calcular_rpa(valor_servico: float, com_iss: bool = True):
    """Calcula RPA para autônomo"""
    resultado = calcular_rpa_autonomo(valor_servico, com_iss)
    return resultado

@router.post("/importar-csv")
async def importar_folha_csv(file: UploadFile = File(...)):
    """Importa funcionários de CSV e retorna folha calculada"""
    # Implementar lógica
    pass
```

**Arquivo CSV exemplo:**
```csv
nome,cpf,salario_bruto,dependentes,tipo
João Silva,123.456.789-00,3000.00,0,clt
Maria Santos,987.654.321-00,2500.00,1,clt
Pedro Autônomo,111.222.333-00,1500.00,0,autonomo
```

**Checkpoint:**
- Endpoints testados e respondendo ✅
- CSV importado e folha gerada ✅
- Resultados validados ✅

---

### **FASE 4: COMPLIANCE FISCAL (Semana 8)**

#### Semana 8: Verificação de Pendências
**Tempo Estimado:** 10-12 horas

**Objetivos:**
- [ ] Integrar API CND Federal (gov.br)
- [ ] Implementar consulta estadual (Sefaz-SP p.ex. com Selenium se necessário)
- [ ] Implementar consulta municipal (prefeitura local)
- [ ] Criar dashboard consolidado
- [ ] Testes end-to-end

**Implementação:**

```python
# compliance/services.py
import requests
from typing import Dict

def consultar_cnd_federal(cnpj: str, token: str) -> Dict:
    """
    Consulta CND Federal via API gov.br
    
    Requer:
    1. Cadastro em https://dev.gov.br
    2. OAuth2 token
    """
    url = "https://api.gov.br/consulta-cnd"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"cnpj": cnpj}
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        
        if response.status_code == 200:
            return {
                "status": "regular",
                "message": "CNPJ sem pendências federais",
                "cnd_url": response.json().get("url_cnd")
            }
        else:
            return {
                "status": "pendencias",
                "message": response.json().get("erro", "Pendências encontradas"),
                "detalhes": response.json()
            }
    except Exception as e:
        return {"status": "erro", "message": f"Erro na consulta: {str(e)}"}

def consultar_cnd_estadual(cnpj: str, inscricao_estadual: str, uf: str = "SP") -> Dict:
    """
    Consulta CND Estadual (São Paulo como exemplo)
    
    Pode usar:
    - Selenium para automação web (se não houver API)
    - API da Sefaz (se disponível)
    """
    # Exemplo simplificado
    if uf == "SP":
        # TODO: Implementar com Selenium ou API Sefaz-SP
        return {
            "status": "nao_implementado",
            "message": "Consulta estadual requer configuração específica"
        }
    else:
        return {"status": "erro", "message": f"UF {uf} não suportada"}

def consultar_certidao_municipal(cnpj: str, municipio: str = "São Paulo") -> Dict:
    """
    Consulta Certidão de Débitos Municipais
    """
    # Exemplo simplificado
    return {
        "status": "nao_implementado",
        "message": "Consulta municipal requer configuração específica da prefeitura"
    }

def consolidar_status_fiscal(cnpj: str, token: str, inscricao_estadual: str, 
                            municipio: str) -> Dict:
    """Consolida status de todas as esferas"""
    federal = consultar_cnd_federal(cnpj, token)
    estadual = consultar_cnd_estadual(cnpj, inscricao_estadual)
    municipal = consultar_certidao_municipal(cnpj, municipio)
    
    return {
        "cnpj": cnpj,
        "federal": federal,
        "estadual": estadual,
        "municipal": municipal,
        "resumo": {
            "regular": federal["status"] == "regular" and 
                      estadual["status"] == "regular" and
                      municipal["status"] == "regular",
            "data_consulta": "2025-10-22"  # Adicionar data real
        }
    }
```

**Rotas REST:**

```python
# compliance/routes.py
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/v1/compliance", tags=["Compliance"])

@router.get("/status")
async def status_fiscal(cnpj: str, token: str = None):
    """Verifica status fiscal consolidado"""
    try:
        status = consolidar_status_fiscal(cnpj, token, "", "São Paulo")
        return status
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/cnd/federal")
async def cnd_federal(cnpj: str, token: str = None):
    """Consulta CND Federal"""
    resultado = consultar_cnd_federal(cnpj, token)
    return resultado

@router.get("/cnd/estadual")
async def cnd_estadual(cnpj: str, inscricao_estadual: str, uf: str = "SP"):
    """Consulta CND Estadual"""
    resultado = consultar_cnd_estadual(cnpj, inscricao_estadual, uf)
    return resultado

@router.get("/cnd/municipal")
async def cnd_municipal(cnpj: str, municipio: str = "São Paulo"):
    """Consulta Certidão Municipal"""
    resultado = consultar_certidao_municipal(cnpj, municipio)
    return resultado
```

**Checkpoint:**
- API gov.br respondendo (ou simulação funcional) ✅
- Dashboard consolidado criado ✅
- Testes passando ✅

---

### **FASE 5: INTEGRAÇÃO BANCÁRIA (Semanas 9-10)**

#### Semana 9: CNAB 240 + Duplicidades
**Tempo Estimado:** 10-12 horas

**Objetivos:**
- [ ] Estudar formato CNAB 240
- [ ] Usar biblioteca `python-cnab`
- [ ] Gerar arquivo de remessa
- [ ] Detectar duplicidades
- [ ] Testes

**Implementação:**

```python
# financeiro/services.py
from python_cnab import CNAB240Pagamento

def gerar_remessa_cnab(pagamentos: list[Dict]) -> str:
    """
    Gera arquivo CNAB 240 para pagamentos
    
    pagamentos = [
        {
            "favorecido_nome": "Empresa X",
            "favorecido_banco": "001",  # Código banco
            "favorecido_agencia": "0001",
            "favorecido_conta": "123456",
            "favorecido_cpf_cnpj": "12.345.678/0001-90",
            "valor": 1000.00,
            "data_pagamento": "2025-10-25"
        }
    ]
    """
    # Criar arquivo CNAB (simplificado)
    try:
        # Usar biblioteca python-cnab
        remessa = CNAB240Pagamento()
        
        for pagto in pagamentos:
            # Adicionar detalhe de pagamento
            pass
        
        return remessa.gerar()  # Retorna string do arquivo
    except Exception as e:
        raise Exception(f"Erro ao gerar CNAB: {str(e)}")

def detectar_duplicidades(pagamentos: list[Dict]) -> list[int]:
    """
    Detecta pagamentos duplicados
    Retorna lista de índices duplicados
    """
    indices_duplicados = []
    
    for i, pgt1 in enumerate(pagamentos):
        for j, pgt2 in enumerate(pagamentos[i+1:], start=i+1):
            # Comparar: valor + data + favorecido
            if (pgt1["valor"] == pgt2["valor"] and
                pgt1["data_pagamento"] == pgt2["data_pagamento"] and
                pgt1["favorecido_cpf_cnpj"] == pgt2["favorecido_cpf_cnpj"]):
                indices_duplicados.extend([i, j])
    
    return list(set(indices_duplicados))

def validar_pagamentos_antes_envio(pagamentos: list[Dict]) -> Dict:
    """Valida lista de pagamentos antes de enviar"""
    duplicados = detectar_duplicidades(pagamentos)
    
    validacoes = {
        "total_pagamentos": len(pagamentos),
        "duplicidades_encontradas": len(duplicados),
        "indices_duplicados": duplicados,
        "pode_enviar": len(duplicados) == 0
    }
    
    return validacoes
```

**Rotas REST:**

```python
# financeiro/routes.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1/pagamentos", tags=["Pagamentos"])

class PagamentoRequest(BaseModel):
    favorecido_nome: str
    favorecido_cpf_cnpj: str
    valor: float
    data_pagamento: str

@router.post("/validar")
async def validar_pagamentos(pagamentos: list[PagamentoRequest]):
    """Valida pagamentos para duplicidades"""
    pagtos_dict = [p.dict() for p in pagamentos]
    validacao = validar_pagamentos_antes_envio(pagtos_dict)
    return validacao

@router.post("/gerar-cnab")
async def gerar_remessa(pagamentos: list[PagamentoRequest]):
    """Gera arquivo CNAB 240"""
    pagtos_dict = [p.dict() for p in pagamentos]
    
    # Validar antes
    validacao = validar_pagamentos_antes_envio(pagtos_dict)
    if not validacao["pode_enviar"]:
        raise HTTPException(status_code=400, 
                          detail=f"Duplicidades encontradas: {validacao['indices_duplicados']}")
    
    try:
        cnab_content = gerar_remessa_cnab(pagtos_dict)
        return {
            "status": "ok",
            "arquivo": cnab_content[:200] + "...",  # Preview
            "tamanho_bytes": len(cnab_content)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/extrato")
async def obter_extrato(data_inicio: str, data_fim: str):
    """Retorna extrato bancário (simulado)"""
    return {
        "periodo": f"{data_inicio} a {data_fim}",
        "transacoes": [],
        "saldo": 0.0
    }
```

**Checkpoint:**
- Arquivo CNAB gerado e validado ✅
- Duplicidades detectadas ✅
- Endpoints testados ✅

---

#### Semana 10: APIs Bancárias + PIX (Conceitual)
**Tempo Estimado:** 8-10 horas

**Objetivos:**
- [ ] Estudar documentação Banco do Brasil (OAuth2, APIs)
- [ ] Implementar consulta de extrato (simulada)
- [ ] Documentar fluxo PIX (DICT, QR Code)
- [ ] Pesquisar Open Banking
- [ ] Consolidar endpoints

**Documentação Conceitual:**

```python
# financeiro/services.py - Conceitos

"""
# APIs Bancárias Modernas no Brasil

## 1. Banco do Brasil (OAuth2)
- Sandbox: https://api.sandbox.bb.com.br
- Requer: Client ID, Client Secret, certificado digital
- Endpoints principais:
  - GET /contas/{numero}/extrato
  - POST /pagamentos/pix
  - GET /pagamentos/{id}/status

## 2. PIX (Banco Central)
- DICT: Diretório de Identificadores de Contas Transacionais
- Tipos de chave: CPF, CNPJ, Email, Telefone, Aleatória
- QR Code: Estático ou Dinâmico
- Autorização: Certificado digital + Open Banking

## 3. Open Banking/Open Finance
- Padrão: Banco Central do Brasil
- Compartilhamento de dados entre instituições
- Requer consentimento do cliente
- Endpoints FIDO2 para autenticação

## 4. Integração Prática
- Usar SDK's dos bancos quando disponíveis
- Certificado digital (A1 ou A3)
- Autenticação mútua (mTLS)
"""

# Exemplo conceitual - Não é implementação real
def consultar_extrato_bb(conta: str, token_acesso: str) -> Dict:
    """
    Consulta extrato BB
    Requer token OAuth2 válido
    """
    # Em produção: usar requests + mTLS
    url = f"https://api.bb.com.br/contas/{conta}/extrato"
    headers = {"Authorization": f"Bearer {token_acesso}"}
    
    # response = requests.get(url, headers=headers, cert=certificado_path)
    # if response.status_code == 200:
    #     return response.json()
    
    # Simulação para fins educacionais
    return {
        "conta": conta,
        "saldo": 10000.00,
        "transacoes": [
            {"data": "2025-10-22", "descricao": "Pix recebido", "valor": 500.00},
            {"data": "2025-10-21", "descricao": "Pagamento fornecedor", "valor": -1000.00}
        ]
    }

def gerar_qr_code_pix_estatico(chave_pix: str, valor: float = None) -> str:
    """
    Gera QR Code PIX estático
    
    Valor: opcional para QR estático
    Em produção: usar API do Banco Central
    """
    # Simplicado: seria necessário usar biblioteca como qrcode + mandatória-brasileira
    return "00020126580014br.gov.bcb.brcode01051.0.063047052D6F6B..."
```

**Checkpoint:**
- Documentação de conceitos ✅
- Simulações funcionando ✅
- Estrutura para integração real preparada ✅

---

### **FASE 6: CONSOLIDAÇÃO (Semana 11)**

#### Semana 11: API Modular + Testes + Documentação
**Tempo Estimado:** 10-12 horas

**Objetivos:**
- [ ] Revisar e refatorar todo código
- [ ] Implementar autenticação básica (API Key ou JWT)
- [ ] Escrever testes de integração end-to-end
- [ ] Gerar documentação completa (Swagger/OpenAPI)
- [ ] Criar fluxo de negócio completo demonstrativo
- [ ] Consolidar em repositório

**Implementação:**

```python
# app/main.py - Revisado
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthCredentials
from fastapi.openapi.utils import get_openapi

# Importar rotas de cada domínio
from app.fiscal.routes import router as fiscal_router
from app.rh.routes import router as rh_router
from app.compliance.routes import router as compliance_router
from app.financeiro.routes import router as financeiro_router

app = FastAPI(
    title="Python Finanças BR-PY API",
    description="API para automação de processos financeiros e fiscais",
    version="1.0.0"
)

# Segurança
security = HTTPBearer()
API_KEY = "sua_chave_secreta_aqui"

async def verificar_api_key(credentials: HTTPAuthCredentials = Depends(security)):
    if credentials.credentials != API_KEY:
        raise HTTPException(status_code=403, detail="API Key inválida")
    return credentials.credentials

# Registrar rotas
app.include_router(fiscal_router)
app.include_router(rh_router)
app.include_router(compliance_router)
app.include_router(financeiro_router)

# Rota de health check
@app.get("/health")
async def health():
    return {"status": "ok", "version": "1.0.0"}

# Customizar documentação OpenAPI
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="Python Finanças BR-PY",
        version="1.0.0",
        routes=app.routes,
    )
    
    openapi_schema["info"]["description"] = """
    API robusta para automação financeira e fiscal no Brasil e Paraguai.
    
    ## Domínios:
    - **Fiscal**: NFS-e, NFTS, gestão de notas
    - **RH**: Folha de pagamento, cálculos salariais
    - **Compliance**: Verificação de pendências fiscais
    - **Financeiro**: Pagamentos, CNAB, PIX
    
    ## Como usar:
    1. Obter API Key
    2. Adicionar header: `Authorization: Bearer <API_KEY>`
    3. Chamar endpoints desejados
    """
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
```

**Testes de Integração End-to-End:**

```python
# tests/test_fluxo_completo.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_fluxo_mes_completo():
    """
    Simula fluxo completo de um mês:
    1. Dia 5: Calcular folha
    2. Dia 6: Gerar CNAB
    3. Dia 7: Verificar compliance
    4. Dia 8: Conciliar pagamentos
    """
    
    api_key = "sua_chave_secreta_aqui"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    # Dia 5: Calcular folha
    folha_payload = {
        "funcionarios": [
            {
                "nome": "João Silva",
                "salario_bruto": 3000.00,
                "dependentes": 0
            }
        ]
    }
    response_folha = client.post("/api/v1/rh/folha", json=folha_payload, headers=headers)
    assert response_folha.status_code == 200
    folha = response_folha.json()
    
    # Dia 6: Gerar CNAB
    pagamentos = [
        {
            "favorecido_nome": "João Silva",
            "favorecido_cpf_cnpj": "123.456.789-00",
            "valor": folha[0]["salario_liquido"],
            "data_pagamento": "2025-10-30"
        }
    ]
    response_cnab = client.post("/api/v1/pagamentos/gerar-cnab", 
                               json=pagamentos, headers=headers)
    assert response_cnab.status_code == 200
    
    # Dia 7: Verificar compliance
    response_compliance = client.get(
        "/api/v1/compliance/status?cnpj=12.345.678/0001-90",
        headers=headers
    )
    assert response_compliance.status_code == 200
    
    # Dia 8: Verificar extrato (simulado)
    response_extrato = client.get(
        "/api/v1/pagamentos/extrato?data_inicio=2025-10-01&data_fim=2025-10-31",
        headers=headers
    )
    assert response_extrato.status_code == 200

def test_emitir_nfse():
    """Testa emissão de NFS-e"""
    headers = {"Authorization": "Bearer sua_chave_secreta_aqui"}
    
    payload = {
        "prestador_cnpj": "12.345.678/0001-90",
        "tomador_cpf_cnpj": "987.654.321-00",
        "descricao_servico": "Consultoria técnica",
        "valor": 1000.00,
        "aliquota_iss": 5.0
    }
    
    response = client.post("/api/v1/nfse/emitir", json=payload, headers=headers)
    assert response.status_code == 200
    assert "nfse_id" in response.json()
```

**Checkpoint:**
- Testes end-to-end passando ✅
- Documentação Swagger completa ✅
- API pronta para uso ✅

---

### **FASE 7: PARAGUAI (Semana 12)**

#### Semana 12: Adaptação para Paraguai
**Tempo Estimado:** 10-12 horas

**Objetivos:**
- [ ] Pesquisar SIFEN (Sistema de Faturação Eletrônica)
- [ ] Implementar DTE (Documento Tributario Eletrônico)
- [ ] Adaptar cálculos de folha para Paraguai
- [ ] Refatorar API para suportar múltiplos países
- [ ] Testes com contexto paraguaio

**Implementação:**

```python
# app/fiscal/models.py - Novo suporte Paraguai
from enum import Enum

class Pais(Enum):
    BRASIL = "BR"
    PARAGUAI = "PY"

class DocumentoFiscal(BaseModel):
    pais: Pais
    tipo: str  # NFS-e (BR), DTE (PY)
    dados: Dict

# app/fiscal/services.py - Factory pattern
def emitir_documento_fiscal(doc: DocumentoFiscal, api_key: str = None):
    """Factory: roteia para implementação correta por país"""
    if doc.pais == Pais.BRASIL:
        return emitir_nfse_focus(doc.dados, api_key)
    elif doc.pais == Pais.PARAGUAI:
        return emitir_dte_sifen(doc.dados, api_key)
    else:
        raise ValueError(f"País {doc.pais} não suportado")

def emitir_dte_sifen(dados: Dict, api_key: str) -> Dict:
    """
    Emite DTE via SIFEN (Paraguai)
    
    SIFEN (Sistema Integrado de Facturación Electrónica Nacional)
    - Plataforma e-Kuatia
    - Requer certificado digital
    - XML assinado
    """
    # Implementação similar ao Brasil
    # URL: https://sifen.set.gov.py/...
    try:
        # Montar XML conforme padrão DTE
        # Assinar com certificado
        # Enviar via SOAP ou REST
        pass
    except Exception as e:
        return {"status": "error", "message": str(e)}

# app/rh/services.py - Cálculos Paraguai
def calcular_folha_paraguay(salario_bruto: float, dependentes: int = 0) -> Dict:
    """
    Calcula folha de pagamento no Paraguai
    
    - IPS: 9% funcionário + 16,5% empresa
    - IRP: 10% flat (8% na faixa mais baixa)
    - Aguinaldo: 1 mês extra anual
    - Sem FGTS/INSS
    """
    ips_funcionario = salario_bruto * 0.09
    irp = calcular_irp_paraguay(salario_bruto, ips_funcionario, dependentes)
    
    salario_liquido = salario_bruto - ips_funcionario - irp
    ips_empresa = salario_bruto * 0.165
    
    return {
        "salario_bruto": salario_bruto,
        "ips_funcionario": ips_funcionario,
        "irp": irp,
        "salario_liquido": salario_liquido,
        "custo_empresa_ips": ips_empresa,
        "moeda": "PYG"  # Guarani
    }

def calcular_irp_paraguay(salario_bruto: float, ips: float, dependentes: int = 0) -> float:
    """IRP (Impuesto a la Renta Personal)"""
    base = salario_bruto - ips - (dependentes * 50000)  # Ajuste por dependente
    
    if base <= 0:
        return 0.0
    elif base <= 5000000:  # Valor fictício
        return base * 0.08
    else:
        return base * 0.10
```

**Rotas Adaptadas para Multi-país:**

```python
# app/fiscal/routes.py - Adaptado
@router.post("/emitir/{pais}")
async def emitir_documento(pais: str, dados: Dict):
    """
    Emite documento fiscal conforme país
    - /emitir/br → NFS-e (Brasil)
    - /emitir/py → DTE (Paraguai)
    """
    if pais == "br":
        # Implementação Brasil
        pass
    elif pais == "py":
        # Implementação Paraguai
        pass
    else:
        raise HTTPException(status_code=400, detail=f"País {pais} não suportado")

# app/rh/routes.py - Adaptado
@router.post("/folha/{pais}")
async def calcular_folha_por_pais(pais: str, dados: SalarioRequest):
    """Calcula folha conforme país"""
    if pais == "br":
        return calcular_folha_brasil(dados)
    elif pais == "py":
        return calcular_folha_paraguay(dados)
```

**Checkpoint:**
- SIFEN integrado (simulado) ✅
- Cálculos paraguaios implementados ✅
- API suportando ambos países ✅
- Estrutura pronta para expansão ✅

---

## 🎓 Como Usar o Claude Pro para Este Plano

### Modelos Recomendados

| Situação | Modelo | Motivo |
|----------|--------|--------|
| Implementar módulos complexos | Claude Sonnet 4.5 | Melhor raciocínio, ótimo para código |
| Consultas rápidas | Claude Sonnet 4 | Mais rápido, economiza tokens |
| Code review profundo | Claude Sonnet 4.5 | Detecta problemas sutis |
| Debugging | Claude Sonnet 4.5 | Melhor análise de problemas |
| Pesquisa teórica | Sonnet 4.5 | Mais contexto |

### Estrutura de Conversas Recomendada

**1. Criar um Projeto por Módulo**
```
Nome: Módulo 3 - NFS-e (Fiscal)
Adicionar arquivos:
- Plano de Aprendizado (PDF)
- Código atual do projeto
```

**2. Prompts Efetivos**

**Para Aprender:**
```
"Explique NFS-e como se eu fosse um desenvolvedor 
iniciante. Use exemplos práticos do código que vou 
implementar. Qual é o primeiro conceito que preciso 
entender?"
```

**Para Implementar:**
```
"Preciso implementar [funcionalidade] do Módulo X.
1. Explique a abordagem
2. Mostre código comentado passo-a-passo
3. Indique 3 casos de teste
4. Aponte erros comuns
Considere meu nível como iniciante."
```

**Para Revisar:**
```
"Revise este código focando em:
- Segurança (dados financeiros sensíveis)
- Performance
- Boas práticas Python
- Casos extremos não tratados
- Sugestões de refatoração"
```

### Checkpoints de Validação

Ao completar cada módulo, peça:

```
"Validação do Módulo X:

1. Me faça 5 perguntas técnicas para testar meu 
   conhecimento

2. Revise o código que produzi, indicando:
   - O que está bom
   - O que melhorar
   - Próximos passos

3. Confirme: Estou pronto para o Módulo X+1?"
```

---

## 📈 Estrutura de Progresso

```
[███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] Semana 1-2  (FASE 1: Fundamentos)
[██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] Semana 3-5  (FASE 2: Fiscal)
[█████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] Semana 6-7  (FASE 3: RH)
[███████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░] Semana 8    (FASE 4: Compliance)
[██████████████░░░░░░░░░░░░░░░░░░░░░░░░░] Semana 9-10 (FASE 5: Bancário)
[██████████████████░░░░░░░░░░░░░░░░░░░░░] Semana 11   (FASE 6: Consolidação)
[█████████████████████░░░░░░░░░░░░░░░░░░] Semana 12   (FASE 7: Paraguai)
[████████████████████████████████████████] Completo!   (12 semanas)
```

---

## 🚀 Próximos Passos Imediatos

### Hoje (Semana 1 - Dia 1):

- [ ] Copiar este arquivo para seu projeto
- [ ] Revisar ferramentas (VSCode, Python 3.10+, Git)
- [ ] Criar pasta `/Python-Financas-BR-PY`
- [ ] Inicializar repositório Git
- [ ] Criar `requirements.txt` inicial:

```txt
fastapi==0.104.1
uvicorn==0.24.0
python-cnab==0.2.1
pynfe==2.0.0
requests==2.31.0
python-dotenv==1.0.0
pytest==7.4.3
pydantic==2.5.0
```

### Próxima semana (Semana 1 - Dias 2-7):

- [ ] Configurar VSCode (extensões Python)
- [ ] Criar primeiro projeto FastAPI
- [ ] Fazer primeiros 3 commits no Git
- [ ] Completar Checkpoint da Semana 1

---

## 📞 Ressources e Referências

### Documentação Oficial
- **FastAPI**: https://fastapi.tiangolo.com/
- **Python**: https://docs.python.org/3/
- **Focus NFe** (NFS-e): https://focusnfe.com.br/doc/
- **PyNFe**: https://pypi.org/project/PyNFe/
- **python-cnab**: https://pypi.org/project/python-cnab/
- **Gov.br (CND)**: https://www.gov.br/conecta/catalogo/apis/

### Comunidades
- Stack Overflow (Python, FastAPI)
- GitHub Discussions
- Comunidades locais Python Brasil

---

## ⚠️ Notas Importantes

### Sobre Dados Sensíveis
- **Nunca** commitar tokens/API keys em repositório
- Usar `.env` com variáveis de ambiente
- Exemplo `.env.example` sem dados reais

### Sobre Implementação Real
- Este plano usa **ambientes de homologação/sandbox**
- Certificados digitais reais requerem **registro legal**
- Produção exige **análise jurídica** adicional

### Continuidade de Aprendizado
- Após Semana 12: Considere Django REST Framework
- Integração com banco de dados real (PostgreSQL)
- Deploy em cloud (AWS, GCP, Azure)
- CI/CD (GitHub Actions, GitLab CI)

---

## 📝 Monitoramento Semanal

Preench esta tabela semanalmente:

| Semana | Módulo | Meta | Completado | Observações |
|--------|--------|------|-----------|------------|
| 1 | Fundamentos | API Hello World | ☐ | |
| 2 | Fundamentos | Estrutura Base | ☐ | |
| 3 | Fiscal | Conceitos + Modelo | ☐ | |
| 4 | Fiscal | API Focus NFe | ☐ | |
| 5 | Fiscal | Integração Completa | ☐ | |
| 6 | RH | Cálculos do Zero | ☐ | |
| 7 | RH | Extensões + API | ☐ | |
| 8 | Compliance | Verificações | ☐ | |
| 9 | Bancário | CNAB + Duplicidades | ☐ | |
| 10 | Bancário | APIs + PIX | ☐ | |
| 11 | Consolidação | Sistema Integrado | ☐ | |
| 12 | Paraguai | Multi-país | ☐ | |

---

**Boa jornada de estudo e desenvolvimento! 🚀**

*Documento versão 1.0 - Atualizar conforme progresso*
