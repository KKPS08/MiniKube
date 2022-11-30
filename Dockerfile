FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y

ADD . /usr/app/src
WORKDIR /usr/app/src

CMD ["python3","./HelloWorldServer.py"]