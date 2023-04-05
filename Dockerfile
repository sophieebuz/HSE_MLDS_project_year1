FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3.10 python3-pip

RUN mkdir /home/service
WORKDIR /home/service

ADD ./requirements.txt /home/service
ADD ./Makefile /home/service

RUN make install_dependencies

CMD ["make", "run_service"]