# Nome do serviço Docker Compose
SERVICE=ifood-lab

# Subir o container com build
build:
	bash create-env-file.sh
	docker-compose up --build

# Subir o container sem rebuild
start:
	docker-compose up

# Parar o container
stop:
	docker-compose down

# Rebuild completo
rebuild:
	docker-compose down
	bash create-env-file.sh
	docker-compose build --no-cache
	docker-compose up

# Ver logs do container
logs:
	docker-compose logs -f $(SERVICE)

# Acessar o bash do container
bash:
	docker exec -it $(SERVICE) /bin/bash

# Rodar Jupyter manualmente (caso precise)
jupyter:
	docker exec -it $(SERVICE) jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password=''

# Checar status dos containers
ps:
	docker ps

# Limpar imagens/paradas (cuidado!)
clean:
	docker system prune -af --volumes
