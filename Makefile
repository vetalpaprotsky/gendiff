install:
	poetry install

test:
	poetry run pytest tests --cov=gendiff

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

publish-test:
	poetry publish -r test-pypi

.PHONY: install test lint selfcheck check build publish-test
