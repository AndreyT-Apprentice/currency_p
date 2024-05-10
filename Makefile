SHELL := /bin/bash

manage_py = python ./app/manage.py

runserver:
	$(manage_py) runserver 0:8000

migrate:
	$(manage_py) migrate

shell_plus:
	$(manage_py) shell_plus --print-sql
