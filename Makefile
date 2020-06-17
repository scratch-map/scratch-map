SONAR_TOKEN?=
GIT_BRANCH=$(shell git rev-parse --abbrev-ref HEAD)

lint:
	pipenv run flake8
	pipenv check ./scratch-map ./tests

sonarscan:
	sonar-scanner \
	  -Dsonar.organization=scratch-map \
	  -Dsonar.projectKey=scratch-map_scratch-map \
	  -Dsonar.branch.name=$(GIT_BRANCH) \
	  -Dsonar.sources=. \
	  -Dsonar.host.url=https://sonarcloud.io \
	  -Dsonar.login=$(SONAR_TOKEN)

test: lint
	pipenv run python run_tests.py

start:
	docker-compose up --no-deps

build:
	docker-compose build
