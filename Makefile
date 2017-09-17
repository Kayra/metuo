.PHONY: all install run database

all:
	-${MAKE} install
	-${MAKE} database
	-${MAKE} run

install:
	pass

database:
ifeq (psql -c "SELECT * FROM pg_database where datname='metuo'", 1)
	@psql -c "CREATE USER metuo WITH PASSWORD 'local_insecure_password';"
	@psql -c "CREATE DATABASE metuo OWNER metuo"
endif

run:
	pass
