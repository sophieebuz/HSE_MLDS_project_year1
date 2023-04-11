FROM python:3.10-buster

RUN mkdir home/service
WORKDIR home/service

COPY requirements.txt ./requirements.txt
COPY main.py ./main.py
COPY test.py ./test.py
COPY feature_engineering.py ./feature_engineering.py
COPY lemmatization.py ./lemmatization.py
COPY model.py ./model.py
COPY analysing.py ./analysing.py

COPY templates/ ./templates/
COPY static/ ./static/
COPY picke_files/ ./picke_files/

ARG POETRY_HOME=/etc/poetry
ENV PATH=${POETRY_HOME}/bin:${PATH}
RUN curl -sSL https://install.python-poetry.org | python -
COPY poetry.lock pyproject.toml ./
RUN poetry install

CMD ["poetry", "run", "uvicorn", "--host", "0.0.0.0", "main:app"]
