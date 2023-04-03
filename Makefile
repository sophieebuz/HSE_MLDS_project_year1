download_data:
ifeq (,$(wildcard ./final_pipeline/data/test_50k.csv))
	mkdir -p ./final_pipeline/data
	test -f ./final_pipeline/data/data.zip || wget --load-cookies ./final_pipeline/data/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies ./final_pipeline/data/cookies.txt--keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1M94kubHLkgf-f0IM7s3HhCKdArNYVbR6' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1M94kubHLkgf-f0IM7s3HhCKdArNYVbR6" -O ./final_pipeline/data/data.zip && rm -f ./final_pipeline/data/cookies.txt
	unzip ./final_pipeline/data/data.zip -d ./final_pipeline/data/
	rm -f ./final_pipeline/data/data.zip
endif

install_dependencies:
	pip install -r requirements.txt

run_service:
	cd service && uvicorn main:app --host 0.0.0.0 --reload

docker_build:
	docker stop mlds_project_container
	docker rm mlds_project_container
	docker build -t mlds_project .
	docker create --name mlds_project_container -p 8000:8000 mlds_project

docker_run:
	docker start mlds_project_container

docker_stop:
	docker stop mlds_project_container

init: install_dependencies download_data