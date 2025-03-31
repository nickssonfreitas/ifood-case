
# 🛒 iFood Case – Recomendação de Ofertas com PySpark

Este projeto tem como objetivo aplicar algoritmos de aprendizado de máquina para recomendar ofertas personalizadas a clientes, utilizando dados de transações, campanhas e perfis de clientes. A solução é construída com Python 3.11, PySpark e bibliotecas modernas de ciência de dados, com um ambiente totalmente automatizado via Docker.

---

## 🚀 Tecnologias utilizadas

- **Python 3.11**
- **PySpark** (>= 3.5.0)
- **Pandas**, **Scikit-learn**, **Matplotlib**, **Seaborn**
- **XGBoost**, **LightGBM**, **CatBoost**
- **JupyterLab**
- **Docker + Docker Compose**
- [`uv`](https://github.com/astral-sh/uv) — gerenciador de dependências moderno e rápido
- `Makefile` para automação de tarefas

---

## 📦 Requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Make](https://www.gnu.org/software/make/) (instalado por padrão no Linux/macOS)

---

## ⚙️ Comandos via Makefile

| Comando         | Descrição                                                                 |
|-----------------|---------------------------------------------------------------------------|
| `make build`    | Gera `.env` e sobe os containers com build                                |
| `make start`    | Sobe os containers sem rebuild                                            |
| `make stop`     | Para todos os containers                                                  |
| `make rebuild`  | Faz rebuild limpo e sobe novamente                                        |
| `make logs`     | Mostra os logs do container `ifood-jupyterlab`                            |
| `make logs-all` | Mostra os logs de todos os serviços                                       |
| `make bash`     | Acessa o terminal do container `ifood-jupyterlab`                         |
| `make jupyter`  | Executa o JupyterLab manualmente dentro do container                      |
| `make ps`       | Mostra o status dos containers em execução                                |
| `make clean`    | ⚠️ Remove containers, volumes e imagens não usadas                        |
| `make lint`     | Roda `ruff`, `black`, `isort` e `mypy` no diretório `src`                 |
| `make test`     | Executa os testes com `pytest`                                            |

---

## 🔧 Setup e execução

### 1. Clone o repositório

```bash
git clone https://github.com/nickssonfreitas/ifood-case.git
cd ifood-case
```

### 2. Construa e inicie o ambiente

```bash
make build
```

Acesse o JupyterLab em: [http://localhost:8888](http://localhost:8888)

---

## 📁 Estrutura do projeto

```text
.
├── src/                       # Código-fonte da solução
├── notebooks/                # Notebooks exploratórios e de modelagem
├── pyproject.toml            # Definição de dependências e configuração do projeto
├── README.md                 # Este arquivo
├── Makefile                  # Comandos automatizados
├── docker-compose.yml        # Orquestração dos containers
├── docker/
│   └── Dockerfile            # Ambiente Docker com Python, Spark e uv
│   └── start_notebook.sh     # Script de inicialização do JupyterLab
└── .dockerignore             # Arquivos ignorados no build da imagem
```

---

## 📚 Desenvolvimento local (sem Docker)

> Opcional para quem quiser rodar localmente

Requer: Python 3.11+ e [uv](https://github.com/astral-sh/uv)

```bash
uv pip compile pyproject.toml -o requirements.txt
uv pip install -r requirements.txt
jupyter lab
```

---

## 🧪 Rodando os testes

```bash
make test
```

---

## 🧼 Lint e estilo de código

Este projeto utiliza:

- [`black`](https://github.com/psf/black) – formatação
- [`isort`](https://pycqa.github.io/isort/) – organização de imports
- [`ruff`](https://github.com/astral-sh/ruff) – linting
- [`mypy`](http://mypy-lang.org/) – verificação de tipos

Para rodar tudo de uma vez:

```bash
make lint
```

---

## 👤 Autor

Nicksson Ckayo Arrais de Freitas  
📧 nickssonarrais@email.com  
🔗 [github.com/nickssonfreitas](https://github.com/nickssonfreitas)

---
