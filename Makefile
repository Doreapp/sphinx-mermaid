PROJECT_NAME=sphinxmermaid
TEST_DIR=tests

PYTHON=python3
DOCKER_IMAGE=${PROJECT_NAME}-docker
DOCKER_RUN=docker run \
 -u $(shell id -u):$(shell id -g) \
 -v $(shell pwd)/$(PROJECT_NAME):/work/$(PROJECT_NAME) \
 -v $(shell pwd)/$(TEST_DIR):/work/$(TEST_DIR)

TWINE_USERNAME=__token__

LINE_LENGTH=100

.PHONY: build doc

all: format lint

help: ## Print help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

clean: ## Remove all the generated files
	@rm -rf *.dist-info *.egg-info
	@rm -rf dist build
	@rm -rf ${PROJECT_NAME}/__pycache__ ${PROJECT_NAME}/*.pyc ${PROJECT_NAME}/*.pyo

format: ## Run isort and black to format Python code
	@${PYTHON} -m isort --line-length ${LINE_LENGTH} --profile black . ${PROJECT_NAME} ${TEST_DIR}
	@${PYTHON} -m black --line-length ${LINE_LENGTH} *.py ${PROJECT_NAME}/**.py ${TEST_DIR}/**.py

lint: ## Check Python code with isort, black and pylint to identify any problem
	${PYTHON} -m isort --line-length ${LINE_LENGTH} --profile black --check . ${PROJECT_NAME} ${TEST_DIR}
	${PYTHON} -m black --line-length ${LINE_LENGTH} --check *.py ${PROJECT_NAME}/**.py ${TEST_DIR}/**.py
	${PYTHON} -m pylint ${PROJECT_NAME}/* ${TEST_DIR}/*

dist: ## Build wheel for the package
	$(PYTHON) setup.py bdist_wheel --universal

upload_dist: ## Upload package to pypi
ifndef TWINE_PASSWORD
	$(error TWINE_PASSWORD must be defined)
endif
	$(PYTHON) -m twine upload dist/*

build: ## Build docker image
	docker build -t $(DOCKER_IMAGE) .

docker_%: ## Run `make %` inside docker container
docker_%: build
	@echo running `make $(shell echo $@ | cut -d_ -f2-)` in docker container
	@$(DOCKER_RUN) $(OPTIONS) \
		-t $(DOCKER_IMAGE) \
		$(shell echo $@ | cut -d_ -f2-)

docker_dist: ## Run `make dist` with docker
docker_dist: build
	mkdir -p dist
	@$(DOCKER_RUN) $(OPTIONS) \
		-v $(shell pwd)/dist:/work/dist \
		-t $(DOCKER_IMAGE) \
		dist

docker_upload_dist: ## Run `make upload_dist` with docker
docker_upload_dist: build
	mkdir -p dist
	@$(DOCKER_RUN) $(OPTIONS) \
		-v $(shell pwd)/dist:/work/dist \
		-e TWINE_PASSWORD \
		-t $(DOCKER_IMAGE) \
		upload_dist

_interactive: ## Enter the docker container in interactive mode
_interactive: build
	$(DOCKER_RUN) --entrypoint /bin/bash -i $(OPTIONS) -t $(DOCKER_IMAGE)

doc: ## Build the documentation
	make -C doc docker_html SPHINXOPTS=$(SPHINXOPTS) O=$(O)
