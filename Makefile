.PHONY: all install run database

all:
	-${MAKE} install
	-${MAKE} database
	-${MAKE} run


install:

ifneq ("$(wildcard $(./venv))",)
	@rm -rf venv/
endif

	@virtualenv -p python3 venv
	@. venv/bin/activate; pip install -r ./requirements.txt


database:

	@psql -c "DROP DATABASE IF EXISTS metuo"
	@psql -c "DROP USER IF EXISTS metuo"
	@psql -c "CREATE USER metuo WITH PASSWORD 'local_insecure_password';"
	@psql -c "CREATE DATABASE metuo OWNER metuo"

	@. venv/bin/activate; \
	export PYTHONPATH=$(shell pwd); \
	python -c "exec(\"from api.app import db\\ndb.create_all()\")"


run:

	@export PYTHONPATH=$(shell pwd); \
	export FLASK_APP=api/app.py; \
	export FLASK_ENV=development; \
	. venv/bin/activate; flask run
