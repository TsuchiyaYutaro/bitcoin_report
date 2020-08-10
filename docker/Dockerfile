FROM python:3.8-alpine

RUN mkdir /code/
WORKDIR /code/

COPY requirements.txt /code/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
