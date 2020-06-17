ORGANISATION=scratch-map
SNYK_TOKEN?=

lint:
	pipenv run flake8
	pipenv check ./scratch-map ./tests

snyk:
	snyk auth $(SNYK_TOKEN)
	snyk monitor --org=$(ORGANISATION)

test: lint
	pipenv run python run_tests.py

start:
	docker-compose up --no-deps

build:
	docker-compose build
