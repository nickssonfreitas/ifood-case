FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

# Argumentos com valores padrão
# Run "id -u" in host and get UID and "id -g" to get "GID
ARG UID=1002
ARG GID=1002 
ARG USERNAME=nicksson

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    default-jdk \
    curl \
    ca-certificates \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instala o UV (antes de qualquer coisa)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto (depois que WORKDIR está definido)
COPY ../ ./

# Instala as dependências do projeto
RUN uv pip install . --system

# Copia o script de entrada do notebook
COPY docker/start_notebook.sh /usr/local/bin/start_notebook.sh
RUN chmod +x /usr/local/bin/start_notebook.sh

# Cria grupo e usuário compatíveis com o host
RUN groupadd -g $GID $USERNAME && \
    useradd -m -u $UID -g $GID -s /bin/bash $USERNAME

# Ajusta permissões do diretório de trabalho
RUN chown -R $USERNAME:$USERNAME /app

# Troca para o usuário
USER $USERNAME

# Define o ponto de entrada
ENTRYPOINT ["start_notebook.sh"]