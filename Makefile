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
	cd service && uvicorn main:app --reload

init: install_dependencies download_data