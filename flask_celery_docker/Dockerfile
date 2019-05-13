FROM python:3.7.3-alpine3.9

RUN apk add --virtual build-dependencies build-base gcc wget git
RUN apk add readline readline-dev zlib-dev perl perl-dev bison flex flex-dev linux-headers postgresql-dev unixodbc-dev
RUN pip install --upgrade pip

RUN pip install celery sqlalchemy psycopg2 flask
RUN mkdir work

COPY . /work
WORKDIR /work

ENTRYPOINT ["/work/entrypoint.sh"]

