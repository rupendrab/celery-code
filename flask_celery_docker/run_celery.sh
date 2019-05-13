#!/bin/bash

ip=172.17.0.1

docker run --rm -d --name my-celery-01 -e RABBIT_IP=${ip} -e POSTGRES_IP=${ip} my-celery
