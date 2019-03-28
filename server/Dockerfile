FROM python:3.7
MAINTAINER Kayra Alat

RUN apt-get update -y

RUN mkdir /server
COPY . /server

RUN pip install --no-cache-dir -r /server/requirements.txt

ENV FLASK_DEBUG 0
ENV FLASK_APP server

EXPOSE 5000

ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]
