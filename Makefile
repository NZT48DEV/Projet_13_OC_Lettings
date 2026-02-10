# Image publiée sur Docker Hub
IMAGE = nzt48dev/oc-lettings

# Tag par défaut (latest)
TAG ?= latest

# Port local:port container
PORT ?= 8000

# Fichier d'env utilisé pour injecter les variables Django
ENV_FILE ?= .env

# Nom du container (utile pour debug / logs)
CONTAINER_NAME = oc-lettings

.PHONY: docker-run docker-run-debug docker-pull docker-stop docker-logs

# Commande unique demandée : pull + run (mode propre, container supprimé à l'arrêt)
docker-run: docker-pull
	docker run --rm \
		-p $(PORT):8000 \
		--env-file $(ENV_FILE) \
		$(IMAGE):$(TAG)

# Mode debug : container nommé, persistant (logs, exec, stop possibles)
docker-run-debug: docker-pull
	docker run \
		--name $(CONTAINER_NAME) \
		-p $(PORT):8000 \
		--env-file $(ENV_FILE) \
		$(IMAGE):$(TAG)

# Récupère la dernière image depuis Docker Hub
docker-pull:
	docker pull $(IMAGE):$(TAG)

# Stop le container debug s'il tourne
docker-stop:
	docker stop $(CONTAINER_NAME) || true

# Suivre les logs du container debug
docker-logs:
	docker logs -f $(CONTAINER_NAME)
