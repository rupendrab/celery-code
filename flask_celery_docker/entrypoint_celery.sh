#!/bin/sh

celery -A celery_example.celery worker --loglevel=info
