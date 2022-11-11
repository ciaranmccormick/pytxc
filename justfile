# run mypy and flake8
lint:
	poetry run mypy pytxc tests/*.py
	poetry run flake8 pytxc tests

# run all the unit tests
test-all:
	poetry run pytest tests/

# run a specific test
test TEST:
  poetry run pytest TEST

# run the checks on the package
check:
	poetry check
	poetry run pip check
	poetry run pip-audit

# run linting, checking and testing
all: lint check test-all
