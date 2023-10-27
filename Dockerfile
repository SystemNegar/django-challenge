FROM python:3.10
LABEL MAINTAINER = "Mahdi Namaki | mavenium@gmail.com"

ENV PYTHONUNBUFFERD 1

RUN mkdir /project
WORKDIR /project
COPY /src /project

ADD requirements_base.txt /project

RUN apt-get -y update
RUN apt-get -y upgrade

RUN pip install --upgrade pip
RUN pip install --upgrade -r requirements_base.txt

RUN apt-get clean