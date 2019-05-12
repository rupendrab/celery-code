#!/bin/bash

cd $(dirname $0)

docker-compose up -d --scale celery-worker=3
