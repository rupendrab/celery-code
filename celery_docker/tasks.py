from celery import Celery
import os
import time

rabbit_ip=os.getenv('RABBIT_IP')
postgres_ip=os.getenv('POSTGRES_IP')

app = Celery('tasks', 
             broker=f'amqp://rupen:secret@{rabbit_ip}/rab1',
             backend=f'db+postgresql://postgres:example@{postgres_ip}/postgres')

@app.task
def reverse(string):
    time.sleep(10)
    return string[::-1]

