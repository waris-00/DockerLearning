from flask import Flask #import 
import redis
import os

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis') # import os library, retrieve redist host from env variables. using OS to get env variables
redis_port = int(os.getenv('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port) #connect to redis database
#r = redis.Redis(host=redis, port=6379) #connect to redis database - can work by manually defining port too

@app.route('/') # create first route (base route)
def welcome(): # define function
    return f'Welcome to the CoderCo Container Challenge.'

@app.route('/count')
def count():
    count = r.incr('visits')
    return f'This page has been visited {count} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)