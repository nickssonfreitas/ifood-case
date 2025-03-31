FROM python:3.11-slim

# Argumentos para usuário não-root
ARG USERNAME=nicksson
ARG UID=1000
ARG GID=1000

# Variáveis de ambiente
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    UV_CACHE_DIR="/home/${USERNAME}/.cache/uv" \
    PATH="/home/${USERNAME}/.local/bin:$PATH"

# Instalar dependências do sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    default-jdk \
    curl \
    git \
    build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Criar usuário não-root
RUN groupadd -g ${GID} ${USERNAME} && \
    useradd -m -s /bin/bash -u ${UID} -g ${GID} ${USERNAME}

# Instalar uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependência e instalar dependências do projeto
COPY --chown=${USERNAME}:${USERNAME} pyproject.toml ./
COPY --chown=${USERNAME}:${USERNAME} README.md ./

RUN uv pip compile pyproject.toml -o requirements.txt && \
    uv pip install --system -r requirements.txt
   
# Copiar restante do projeto e script de inicialização
COPY --chown=${USERNAME}:${USERNAME} . .
COPY docker/start_notebook.sh /usr/local/bin/start_notebook.sh
RUN chmod +x /usr/local/bin/start_notebook.sh

# Ajustar permissões
RUN chown -R ${USERNAME}:${USERNAME} /app

# Trocar para usuário não-root
USER ${USERNAME}

# Entrypoint para iniciar o JupyterLab com suporte ao PySpark
ENTRYPOINT ["start_notebook.sh"]