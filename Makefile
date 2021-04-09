SHELL := /bin/bash

manage_py := python app/manage.py

activate:
	source env/bin/activate

runserver:
	$(manage_py) runserver

run_celery:
	app/celery -A booksharing worker -l info

migrate:
	$(manage_py) migrate

makemigrations:
	$(manage_py) makemigrations

shell_plus:
	$(manage_py) shell_plus --print-sql