install-dev:
	pipenv install --dev

install:
	pipenv install

lint:
	pipenv run flake8
	pipenv check ./scratch-map ./tests

test: lint
	pipenv run python run_tests.py

start:
	docker-compose up --no-deps

build:
	docker-compose build
