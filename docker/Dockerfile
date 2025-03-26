# Imagem base com Python 3.11
FROM python:3.11-slim

# Evita prompts interativos durante a instalação
ENV DEBIAN_FRONTEND=noninteractive

# Define o nome do usuário
ARG USERNAME=nicksson

# Atualiza pacotes e instala dependências do sistema
RUN apt-get update && apt-get install -y \
    default-jdk \
    curl \
    ca-certificates \
    git \
    tmux \
    nano\
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instala o UV via script oficial (https://docs.astral.sh/uv/guides/integration/docker/#configuring-watch-with-docker-compose)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Cria um usuário não root e define permissões
RUN useradd -ms /bin/bash $USERNAME

# Define o diretório de trabalho no container
WORKDIR /app

# Copia todos os arquivos do projeto
COPY . .

# Ajusta as permissões dos arquivos para o usuário não root
RUN chown -R $USERNAME:$USERNAME /app

# Troca para o usuário não root
USER $USERNAME

# Instala as dependências diretamente no Python da venv usando UV
RUN uv pip install . --system

# Ajusta as permissões do diretório de trabalho para o usuário não root
RUN chmod -R 755 /app

# Expondo a porta do JupyterLab
EXPOSE 8888

# Comando padrão do container
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]