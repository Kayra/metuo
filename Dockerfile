FROM python:3.7
MAINTAINER Kayra Alat

RUN apt-get update -y

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=api/app.py

EXPOSE 5000
