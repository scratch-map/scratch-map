SONAR_TOKEN?=
GIT_BRANCH?=$(shell git rev-parse --abbrev-ref HEAD)

# Other
install:
	pipenv install

# Dev
init:
	pip install pipenv --upgrade
	pipenv install --dev
	pre-commit install

local:
	pipenv run python run.py

clean:
	pipenv clean
	rm -rf .scannerwork
	rm -rf .pytest_cache
	rm -rf **/.pytest_cache

# Code Quality
lint:
	pipenv run flake8
	pipenv check ./scratch-map ./tests

test:
	pipenv run python run_tests.py

sonarscan:
	sonar-scanner \
	  -Dsonar.organization=scratch-map \
	  -Dsonar.projectKey=scratch-map_scratch-map \
	  -Dsonar.branch.name=$(GIT_BRANCH) \
	  -Dsonar.sources=. \
	  -Dsonar.host.url=https://sonarcloud.io \
	  -Dsonar.login=$(SONAR_TOKEN)

# Deployment
build:
	docker-compose build

start:
	docker-compose up --no-deps
