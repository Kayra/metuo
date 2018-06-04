.PHONY: all install run database


install:

	-${MAKE} dotenv
	docker-compose up
	-${MAKE} database


start:

	docker-compose up


database:

	docker exec -it metuo_app_1 python create_database.py


dotenv:

	@printf "POSTGRES_DB=metuo\n \
			 POSTGRES_USER=metuo\n \
          	 POSTGRES_PASSWORD=local_insecure_password\n \
          	 FLASK_DEBUG=1" \
    | tr -d "[:blank:]" \
    > .env
