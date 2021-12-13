FROM python:3.9-alpine as base

WORKDIR  /app
COPY ./app/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./app/ /app/
WORKDIR /

ENV FLASK_APP=app
EXPOSE 5000
CMD flask run -h 0.0.0 -p 5000