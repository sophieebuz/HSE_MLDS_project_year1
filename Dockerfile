FROM python:3.10

RUN apt-get update
#RUN apt-get install -y python3.10 python3-pip

RUN mkdir /home/service
WORKDIR /home/service

ADD ./poetry.lock /home/service
ADD ./pyproject.toml /home/service
ADD ./Makefile /home/service

ARG POETRY_HOME=/opt/poetry
ENV PATH=${POETRY_HOME}/bin:${PATH}
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN make install_dependencies

CMD ["make", "run_service"]
