# 🐍 Imagem base com Python 3.11
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

# Instala o UV via script oficial
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Garante que o UV esteja no PATH
ENV PATH="/root/.local/bin/:$PATH"

# Define o diretório de trabalho no container
WORKDIR /app

# Copia todos os arquivos do projeto
COPY . .

# Cria o ambiente virtual
RUN uv venv

# Instala as dependências no Python da venv
RUN uv pip install . --python .venv/bin/python

# Expondo a porta do JupyterLab
EXPOSE 8888

# Comando padrão do container (executa diretamente da venv, sem ativar)
CMD [".venv/bin/jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
