SHELL:=/usr/bin/env bash

lint_python:
	flake8 .
	 mypy .

lint_django:
	# check migrations graph
	python manage.py makemigrations --dry-run --check
	# run django check
	python manage.py check --fail-level=WARNING

unit:
	pytest \
		--cov=. \
		--junitxml=/app/.tests_reports/junit.xml

lint_package:
    # TODO: switch to poetry and add
    #	poetry check
	pip check

test: \
	lint_python \
	lint_django \
	unit \
	lint_package
