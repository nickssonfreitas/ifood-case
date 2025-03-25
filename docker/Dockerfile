# Imagem base com Python 3.11
FROM python:3.11-slim

# Evita prompts interativos durante a instalação
ENV DEBIAN_FRONTEND=noninteractive

# Atualiza pacotes e instala dependências do sistema
RUN apt-get update && apt-get install -y \
    default-jdk \
    curl \
    ca-certificates \
    git \
    build-essential \
    && apt-get clean

# Instala o UV via script oficial (https://docs.astral.sh/uv/guides/integration/docker/#configuring-watch-with-docker-compose)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Define o diretório de trabalho no container
WORKDIR /app

# Copia todos os arquivos do projeto
COPY . .

# Instala as dependências diretamente no Python da venv usando UV
RUN uv pip install . --system

# Expondo a porta do JupyterLab
EXPOSE 8888

# Comando padrão do container
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
