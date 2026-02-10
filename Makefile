# Image publiée sur Docker Hub
IMAGE = nzt48dev/oc-lettings

# Tag par défaut (latest)
TAG ?= latest

# Port local:port container
PORT ?= 8000

# Fichier d'env utilisé pour injecter les variables Django
ENV_FILE ?= .env

.PHONY: docker-run docker-run-debug docker-pull docker-stop docker-logs

# Commande unique demandée : pull + run via Docker uniquement
docker-run: docker-pull
	docker run --rm -p $(PORT):8000 --env-file $(ENV_FILE) $(IMAGE):$(TAG)

docker-run-debug: docker-pull
	docker run -p $(PORT):8000 --env-file $(ENV_FILE) $(IMAGE):$(TAG)

docker-pull:
	docker pull $(IMAGE):$(TAG)

# (optionnel) si on utilise la commande docker-run-debug (sans --rm), utile pour debug.
docker-stop:
	docker stop oc-lettings || true

docker-logs:
	docker logs -f oc-lettings
