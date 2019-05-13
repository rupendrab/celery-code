from flask import Flask
from flask_celery import make_celery
import os

rabbit_ip=os.getenv('RABBIT_IP')
postgres_ip=os.getenv('POSTGRES_IP')

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = f'amqp://rupen:secret@{rabbit_ip}/rab1'
app.config['CELERY_BACKEND'] = f'db+postgresql://postgres:example@{postgres_ip}/postgres'

celery = make_celery(app)

@app.route('/process/<name>')
def process(name):
    reverse.delay(name)
    return f'I sent an async request for {name}'

@celery.task(name='celery_example.reverse')
def reverse(string):
    return string[::-1]

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

