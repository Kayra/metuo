.PHONY: install start restart database dotenv servershell psqlshell testunit testinteg teste2e testall


install:
	-${MAKE} dotenv
	docker-compose up
	-${MAKE} database


start:
	@docker-compose up


restart:
	@docker-compose down; \
	docker rmi -f metuo_server; \
	docker-compose up


database:
	@docker exec -it metuo_server_1 flask init-db


dotenv:
	@printf "POSTGRES_DB=metuo\n \
			 POSTGRES_USER=metuo\n \
          	 POSTGRES_PASSWORD=local_insecure_password\n \
          	 FLASK_DEBUG=1" \
    | tr -d "[:blank:]" \
    > .env


servershell:
	@docker exec -it metuo_server_1 bash


psqlshell:
	@docker exec -it metuo_postgres_1 psql metuo metuo


testunit:
	@docker exec -it metuo_server_1 pytest server/tests/unit -p no:warnings


testinteg:
	@docker exec -it metuo_server_1 pytest server/tests/integration -p no:warnings

teste2e:
	@docker exec -it metuo_server_1 pytest server/tests/e2e -p no:warnings

testall:
	make testunit
	make testinteg
	make teste2e
