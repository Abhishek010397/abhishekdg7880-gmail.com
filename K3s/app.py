import time
import redis
from flask import Flask
app = Flask(app)
cache = redis.Redis(host='redis',port 6397)
def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries ==0:
                raise exc
            retries -=1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello world .\n'.format(count)

if app == "__main__":
    app.run(host="0.0.0.0",debug=True)