PROJECT_NAME=sphinxmermaid
TEST_DIR=tests

PYTHON=python3

LINE_LENGTH=100

all: format lint

help: ## Print help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

clean: ## Remove all the generated files
	@rm -rf *.dist-info *.egg-info
	@rm -rf ${PROJECT_NAME}/__pycache__ ${PROJECT_NAME}/*.pyc ${PROJECT_NAME}/*.pyo

format: ## Run isort and black to format Python code
	@${PYTHON} -m isort --line-length ${LINE_LENGTH} --profile black . ${PROJECT_NAME} ${TEST_DIR}
	@${PYTHON} -m black --line-length ${LINE_LENGTH} *.py ${PROJECT_NAME}/* ${TEST_DIR}/*

lint: ## Check Python code with isort, black and pylint to identify any problem
	${PYTHON} -m isort --line-length ${LINE_LENGTH} --profile black --check . ${PROJECT_NAME} ${TEST_DIR}
	${PYTHON} -m black --line-length ${LINE_LENGTH} --check *.py ${PROJECT_NAME}/* ${TEST_DIR}/*
	${PYTHON} -m pylint ${PROJECT_NAME}/* ${TEST_DIR}/*
