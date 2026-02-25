# ============================================================
# Configuration
# ============================================================

IMAGE = nzt48dev/oc-lettings
TAG ?= latest

PORT ?= 8000
ENV_FILE ?= .env
CONTAINER_NAME = oc-lettings

# Mode disponible : default | logs
# Usage :
#   make docker-run-local
#   make docker-run-local MODE=logs
MODE ?= default


# ============================================================
# Commande Gunicorn
# ============================================================

GUNICORN = gunicorn oc_lettings_site.wsgi:application \
	--bind 0.0.0.0:8000 \
	--worker-class gthread \
	--workers 2 \
	--threads 4 \
	--timeout 120 \
	--keep-alive 5

GUNICORN_LOGS = $(GUNICORN) \
	--access-logfile - \
	--error-logfile -

ifeq ($(MODE),logs)
	RUN_CMD = $(GUNICORN_LOGS)
else
	RUN_CMD = $(GUNICORN)
endif


.PHONY: docker-build docker-run-local docker-run docker-run-debug docker-pull docker-stop docker-logs


# ============================================================
# Workflow local (Dockerfile courant)
# ============================================================

docker-build:
	docker build -t oc-lettings-local .

docker-run-local: docker-build
	docker run --rm \
		-p $(PORT):8000 \
		--env-file $(ENV_FILE) \
		oc-lettings-local \
		$(RUN_CMD)


# ============================================================
# Workflow image Docker Hub
# ============================================================

docker-run: docker-pull
	docker run --rm \
		-p $(PORT):8000 \
		--env-file $(ENV_FILE) \
		$(IMAGE):$(TAG)

docker-run-debug: docker-pull
	docker run \
		--name $(CONTAINER_NAME) \
		-p $(PORT):8000 \
		--env-file $(ENV_FILE) \
		$(IMAGE):$(TAG)


# ============================================================
# Utilitaires
# ============================================================

docker-pull:
	docker pull $(IMAGE):$(TAG)

docker-stop:
	docker stop $(CONTAINER_NAME) || true

docker-logs:
	docker logs -f $(CONTAINER_NAME)