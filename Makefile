# Nome do serviço principal do docker-compose (como definido no container_name)
SERVICE=ifood-jupyterlab

# Subir o container com build + criação do .env
build:
	bash create-env-file.sh
	docker-compose up --build

# Subir o container sem rebuild
start:
	docker-compose up

# Parar todos os containers
stop:
	docker-compose down

# Rebuild completo
rebuild:
	docker-compose down --remove-orphans
	bash create-env-file.sh
	docker-compose build --no-cache
	docker-compose up

# Logs apenas do serviço principal (JupyterLab)
logs:
	docker-compose logs -f $(SERVICE)

# Logs de todos os containers
logs-all:
	docker-compose logs -f

# Acessar bash do container principal
bash:
	docker exec -it $(SERVICE) /bin/bash

# Executar Jupyter manualmente (útil se container estiver rodando com command neutro)
jupyter:
	docker exec -it $(SERVICE) jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password=''

# Ver containers ativos
ps:
	docker ps

# Limpeza total (cuidado)
clean:
	@echo "⚠️  Isso vai apagar containers, volumes e imagens não utilizados!"
	sleep 2
	docker system prune -af --volumes

# Rodar lint usando ferramentas configuradas no pyproject
lint:
	docker exec -it $(SERVICE) bash -c "ruff src && black --check src && isort --check-only src && mypy src"

# Rodar testes
test:
	docker exec -it $(SERVICE) pytest
