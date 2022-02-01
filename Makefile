clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

run: clean
	@python manage.py runserver

makemigrations:
	@python manage.py makemigrations

migrate:
	@python manage.py migrate

docker-build:
	@docker-compose build

docker-run:
	@docker-compose up -d

docker-migrate:
	@docker exec -it cronos-backend make migrate

docker-test:
	@docker exec -it cronos-backend make test

flake8:
	@flake8 --show-source .

check-python-import:
	@isort --check-only .

fix-python-import:
	@isort .

lint: clean flake8 check-python-import

test: clean
	@pytest -x .
