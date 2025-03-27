#!/bin/bash

# Exibe mensagem no log
echo "🚀 Iniciando JupyterLab..."

# Executa o JupyterLab com argumentos padrão
exec jupyter lab \
  --ip=0.0.0.0 \
  --port=8888 \
  --no-browser \
  --NotebookApp.token='' \
  --NotebookApp.password='' \
  --allow-root
