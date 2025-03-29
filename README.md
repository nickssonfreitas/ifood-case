# 🧠 iFood Case Técnico – Recomendação de Ofertas com PySpark

Este projeto propõe uma solução baseada em dados para otimizar a estratégia de envio de ofertas aos clientes do iFood, levando em conta o tipo de oferta, o perfil do cliente, canais de marketing e o timing ideal de envio.

---

## 🎯 Objetivo

- Analisar dados históricos de clientes, ofertas e transações
- Construir um modelo que recomende a melhor oferta para cada cliente
- Demonstrar impacto potencial no engajamento e conversão

---

## 📁 Estrutura do Projeto

```
ifood-case/
├── data/
│   ├── raw/               # Dados originais
│   └── processed/         # Dados tratados
├── notebooks/             # Jupyter notebooks
├── presentation/          # Slides para stakeholders
├── src/                   # Módulos Python (ETL, features, etc.)
├── docker/                # Dockerfile
├── docker-compose.yml     # Ambiente com JupyterLab
├── pyproject.toml         # Configuração do projeto Python
├── README.md              # Este arquivo
└── .gitignore
```

---

## ⚙️ Instalação para Desenvolvimento Local com `uv`

> O projeto usa o [uv](https://github.com/astral-sh/uv) como gerenciador de ambientes e dependências via `pyproject.toml`.

### 🔹 Pré-requisitos

- Python 3.11+
- [uv instalado](https://github.com/astral-sh/uv) (`curl -Ls https://astral.sh/uv/install.sh | sh`)

### 🔹 Passos

1. Clone o repositório:

```bash
git clone https://github.com/nickssonfreitas/ifood-case.git
cd ifood-case
```

2. Crie e ative o ambiente virtual com `uv`:

```bash
uv venv
source .venv/bin/activate
```

3. Instale as dependências definidas no `pyproject.toml`:

```bash
uv pip install .
```

4. Inicie o JupyterLab:

```bash
jupyter lab
```

---

## 🐳 Execução com Docker + Docker Compose

> Ideal para rodar o ambiente completo com todas as dependências já configuradas.

### 🔹 Passos

1. Clone o repositório:

```bash
git clone https://github.com/nickssonfreitas/ifood-case.git
cd ifood-case
```

2. Construa e suba os containers:

```bash
make build
```

3. Acesse o JupyterLab:

```
http://localhost:8888/lab
```

---

## 📊 Requisitos dos Dados

Os seguintes arquivos `.json` devem estar salvos na pasta `data/raw/`:

- `offers.json`
- `customers.json`
- `transactions.json`

---

## 🧠 Tecnologias Utilizadas

- Python 3.11
- [uv](https://github.com/astral-sh/uv)
- PySpark
- Pandas
- Scikit-learn
- JupyterLab
- Docker / Docker Compose
- pyproject.toml (PEP 621)

---

## 👥 Público-Alvo da Apresentação

A apresentação de resultados será feita em até **5 slides**, direcionada a **gestores de negócio não técnicos**, com foco em:

- Resultados e projeções
- Impacto da recomendação personalizada
- Ganhos estimados em conversão e engajamento

---

## 📌 Autor

Projeto desenvolvido por **Nicksson Ckayo Arrais de Freitas**  
GitHub: [@nickssonfreitas](https://github.com/nickssonfreitas)  
