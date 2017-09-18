.PHONY: all install run database

all:
	-${MAKE} install
	-${MAKE} database
	-${MAKE} run

install:
	pass

database:
#	DB := $(psql -c "SELECT * FROM pg_database where datname='metuo'")
#	psql -c "SELECT * FROM pg_database where datname='metuo'"
ifneq ($(psql -c "SELECT * FROM pg_roles WHERE rolname='metuo'"),)
	@psql -c "CREATE USER metuo WITH PASSWORD 'local_insecure_password';"
endif

ifneq ($(psql -c "SELECT * FROM pg_database where datname='metuo'"),)
	@psql -c "DROP DATABASE metuo"
endif

	@psql -c "CREATE DATABASE metuo OWNER metuo"

run:
	pass
