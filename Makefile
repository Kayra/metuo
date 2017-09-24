.PHONY: all install run database

all:
	-${MAKE} install
	-${MAKE} database
	-${MAKE} run


install:

ifneq ("$(wildcard $(./venv))",)
	@rm -rf ./venv
endif

	@virtualenv -p python3 venv
	@. ./venv/bin/activate; pip install -r ./requirements.txt


database:

	@psql -c "DROP DATABASE IF EXISTS metuo"
	@psql -c "DROP USER IF EXISTS metuo"
	@psql -c "CREATE USER metuo WITH PASSWORD 'local_insecure_password';"
	@psql -c "CREATE DATABASE metuo OWNER metuo"


run:

	@export FLASK_APP=api/app.py \
	@. ./venv/bin/activate; python -m flask run
