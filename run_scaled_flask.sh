#!/bin/bash

cd $(dirname $0)

docker-compose -f docker-compose-flask.yml up -d --scale celery-worker=3
