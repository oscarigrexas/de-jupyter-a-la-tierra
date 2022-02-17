.DEFAULT_GOAL := help
#OPENAPI_SCHEMA := "docs/openapi.json"
#OPENAPI_COMMIT_MSG := "docs: update OpenAPI schema"
DOCKER_IMAGE_TAG := catfood
DOCKER_CONTAINER_TAG := catfood
DOCKER_DATA_VOLUME_TAG := catfood_data

install-requirements: ## pip install kedro and then use it to install the rest of the requirements
	pip install kedro
	kedro install

run-api: ## run the api locally
	PYTHONPATH=$(PYTHONPATH):$(PWD)/src bash -c 'python src/catfood/api'

test: ## run tests
	kedro test --verbosity=1 --no-cov

test-cov: ## run tests with coverage report
	kedro test --verbosity=1

docker-build: ## run docker build to create docker image
	docker build . -t $(DOCKER_IMAGE_TAG)

docker-run-dev:
	docker run --name $(DOCKER_CONTAINER_TAG) -p 1234:1234 --rm --env-file=.env -v $(DOCKER_DATA_VOLUME_TAG):/home/kedro/data -t $(DOCKER_IMAGE_TAG)

docker-stop:
	docker stop $(DOCKER_CONTAINER_TAG)

docker-enter-container:
	docker exec -it $(DOCKER_CONTAINER_TAG) /bin/bash

docker-clean: ## remove docker image
	docker rmi $(DOCKER_IMAGE_TAG) || exit 0

help: ## display Makefile help
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'