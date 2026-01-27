# 📈 Market Insight Automation

**Automação de Análise do Mercado Financeiro com Python**

## 📌 Visão Geral

Este projeto é um sistema em Python que automatiza a **coleta, processamento e consolidação de dados financeiros públicos**, juntamente com **notícias econômicas**, para auxiliar na análise e acompanhamento do mercado de capitais.

O objetivo é reduzir trabalho manual e fornecer **insights claros e organizados** a partir de dados reais do mercado, utilizando boas práticas de engenharia de software.

---

## 🎯 Motivação

Sempre tive interesse pelo mercado de capitais e por automação de sistemas.

A partir disso, desenvolvi este projeto para unir **programação, dados financeiros e análise automatizada**, simulando um cenário real encontrado em fintechs, bancos e startups.

---

## ⚙️ Funcionalidades (MVP)

- 📊 Coleta automática de dados históricos de ações
- 🧹 Limpeza e padronização dos dados
- 📈 Cálculo de métricas financeiras básicas:
    - Retorno
    - Média móvel
    - Volatilidade
- 📰 Coleta de notícias relacionadas a empresas ou ao mercado
- 📄 Geração automática de relatório (Excel / CSV)
- 🌐 API REST para consulta dos dados processados

---

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Pandas**
- **yFinance**
- **FastAPI**
- **Matplotlib**
- **Git**

---

## 🗂️ Estrutura do Projeto

```
market_insight_automation/
│
├── data/
│   ├── raw/          # dados brutos coletados
│   └── processed/    # dados tratados
│
├── app/
│   ├── main.py       # aplicação FastAPI
│   ├── market_data.py
│   ├── news.py
│   ├── analysis.py
│   └── report.py
│
├── notebooks/
│   └── exploration.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore

```

---

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/market_insight_automation.git
cd market_insight_automation

```

### 2️⃣ Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt

```

### 4️⃣ Executar a aplicação

```bash
uvicorn app.main:app --reload

```

---

## 🌐 Endpoints da API (exemplo)

- `GET /stocks/{ticker}` → dados processados de uma ação
- `GET /summary` → resumo geral do mercado
- `GET /news/{ticker}` → notícias relacionadas

---

## 🔮 Próximos Passos (Evolução para IA)

- Análise de sentimento de notícias (NLP)
- Criação de score de risco por ativo
- Classificação de ativos com base em métricas quantitativas e textuais
- Dashboard interativo
- Transformação em produto SaaS

---

## ⚠️ Aviso Legal

Este projeto tem finalidade **educacional e demonstrativa**.

Não constitui recomendação de investimento.

---

## 👤 Autor

**[Matheus Lunguinho Marchetti]**

Desenvolvedor Python | Automação | Dados & IA
