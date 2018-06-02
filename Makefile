.PHONY: all install run database

all:
	-${MAKE} dotenv
	-${MAKE} database
	-${MAKE} run


install:

ifneq ("$(wildcard $(./venv))",)
	@rm -rf venv/
endif

	@virtualenv -p python3 venv
	@. venv/bin/activate; pip install -r ./requirements.txt


database:

	docker exec -it metuo_app_1 python create_database.py


run:

	@export PYTHONPATH=$(shell pwd); \
	export FLASK_APP=api/app.py; \
	export FLASK_ENV=development; \
	. venv/bin/activate; flask run


dotenv:

	@printf "POSTGRES_DB=metuo\n \
			 POSTGRES_USER=metuo\n \
          	 POSTGRES_PASSWORD=local_insecure_password\n \
          	 FLASK_DEBUG=1" \
    | tr -d "[:blank:]" \
    > .env
