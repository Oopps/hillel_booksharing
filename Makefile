SHELL := /bin/bash

manage_py := python app/manage.py

activate:
	source env/bin/activate

runserver:
	$(manage_py) runserver

migrate:
	$(manage_py) migrate

makemigrations:
	$(manage_py) makemigrations