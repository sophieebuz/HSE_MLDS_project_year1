FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3.10 python3-pip

RUN mkdir home/service
WORKDIR home/service

ADD requirements.txt ./requirements.txt
ADD main.py ./main.py
ADD test.py ./test.py
ADD feature_engineering.py ./feature_engineering.py
ADD lemmatization.py ./lemmatization.py
ADD model.py ./model.py
ADD analysing.py ./analysing.py

ADD templates/ ./templates/
ADD static/ ./static/
ADD picke_files/ ./picke_files/

RUN pip install -r requirements.txt

CMD ["uvicorn", "--host", "0.0.0.0", "main:app", "--reload"]