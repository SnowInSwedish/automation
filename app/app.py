from flask import Flask, render_template
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = cache.incr('hits')
    return render_template('index.html', hits=count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)