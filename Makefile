SONAR_TOKEN?=
GIT_BRANCH?=$(shell git rev-parse --abbrev-ref HEAD)

init:
	pip install pipenv --upgrade
	pipenv install --dev
	pre-commit install

install-dev:
	pipenv install --dev

install:
	pipenv install

lint:
	pipenv run flake8
	pipenv check ./scratch-map ./tests

sonarscan:
	sonar-scanner \
	  -Dsonar.organization=scratch-map \
	  -Dsonar.projectKey=scratch-map_scratch-map \
	  -Dsonar.branch.name=$(GIT_BRANCH) \
	  -Dsonar.sources=. \
	  -Dsonar.python.coverage.reportPaths=coverage.xml \
	  -Dsonar.host.url=https://sonarcloud.io \
	  -Dsonar.login=$(SONAR_TOKEN)

test: lint
	pipenv run coverage run --source scratch_map -m pytest
	pipenv run coverage xml

start:
	docker-compose up --no-deps

build:
	docker-compose build
