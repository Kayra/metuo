.PHONY: install start restart database dotenv servershell psqlshell testunit testinteg teste2e testall


install:
	-${MAKE} dotenv
	docker-compose up


database:
	@docker exec -it metuo_server_1 flask init-db


start:
	@docker-compose up


restart:
	@docker-compose down; \
	docker rmi -f metuo_server; \
	docker-compose up --remove-orphans


dotenv:
	@printf "RDS_DB_NAME=metuo\n \
			 RDS_USERNAME=metuo\n \
          	 RDS_PASSWORD=local_insecure_password\n \
          	 RDS_HOSTNAME=postgres\n \
          	 RDS_PORT=5432\n \
          	 FLASK_DEBUG=1\n \
          	 IMAGE_DIRECTORY=/image_uploads\n \
          	 AWS_ACCESS_KEY_ID=\n \
             AWS_SECRET_ACCESS_KEY=\n \
             AWS_DEFAULT_REGION=eu-west-2\n \
             POSTGRES_DB=metuo\n \
             POSTGRES_USER=metuo\n \
             POSTGRES_PASSWORD=local_insecure_password\n \
             PYTHON_ENV=local\n \
             JWT_SECRET_KEY=dev_secret" \
    | tr -d "[:blank:]" \
    > .env


servershell:
	@docker exec -it metuo_server_1 bash


psqlshell:
	@docker exec -it metuo_postgres_1 psql metuo metuo


testunit:
	@docker exec -it metuo_server_1 pytest server/tests/unit -p no:warnings -vv


testinteg:
	@docker exec -it metuo_server_1 pytest server/tests/integration -p no:warnings


teste2e:
	@docker exec -it metuo_server_1 pytest server/tests/e2e -p no:warnings


testall:
	-${MAKE} testunit
	-${MAKE} testinteg
	-${MAKE} teste2e
