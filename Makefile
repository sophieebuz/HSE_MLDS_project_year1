ROOT_DIR := $(dir $(realpath $(lastword $(MAKEFILE_LIST))))

download_data:
ifeq (,$(wildcard ./final_pipeline/data/test_50k.csv))
	mkdir -p ./final_pipeline/data
	test -f ./final_pipeline/data/data.zip || wget --load-cookies ./final_pipeline/data/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies ./final_pipeline/data/cookies.txt--keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1MUygcOKG_eh1XS5jx4kisjGtfx0tZV8r' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1MUygcOKG_eh1XS5jx4kisjGtfx0tZV8r" -O ./final_pipeline/data/data.zip && rm -f ./final_pipeline/data/cookies.txt
	unzip ./final_pipeline/data/data.zip -d ./final_pipeline/data/
	rm -f ./final_pipeline/data/data.zip
endif

init: install_dependencies download_data

install_dependencies:
	poetry install

run_service:
	poetry run uvicorn service.main:app --host 0.0.0.0 --reload

docker_build:
	docker stop mlds_project_container
	docker rm mlds_project_container
	docker build -t mlds_project .
	docker create -v $(ROOT_DIR):/home/service:rw --name mlds_project_container -p 8000:8000 mlds_project

docker_start:
	docker start mlds_project_container

docker_stop:
	docker stop mlds_project_container

docker_prod_build:
	docker build -f ./Dockerfile_prod  -t mlds_project_prod .

docker_prod_push:
	docker tag mlds_project_prod annaivantsova/hse_mlds_project_year1_service:latest
	docker push annaivantsova/hse_mlds_project_year1_service:latest

docker_prod_run:
	docker run --rm -it --name mlds_project_container_prod -p 8000:8000 mlds_project_prod
