FROM python:3.7
MAINTAINER Kayra Alat

RUN apt-get update -y

RUN mkdir /server
COPY . /server
WORKDIR /server

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=api

EXPOSE 5000
