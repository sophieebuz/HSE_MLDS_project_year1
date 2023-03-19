download_data:
ifeq (,$(wildcard ./data/test_50k_texts.csv))
	mkdir -p ./data
	test -f ./data/data.zip || wget --load-cookies ./data/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies ./data/cookies.txt--keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1M2clIfri1zjXxc-5bWiP3waYq6w9lK1d' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1M2clIfri1zjXxc-5bWiP3waYq6w9lK1d" -O ./data/data.zip && rm -f ./data/cookies.txt
	unzip ./data/data.zip -d ./data/
	rm -f ./data/data.zip
endif

install_dependencies:
	pip install -r requirements.txt

init: install_dependencies download_data