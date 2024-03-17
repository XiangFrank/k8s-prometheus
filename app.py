from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import time

app = Flask(__name__)

connections_counter = Counter('web_connections_total', 'Total number of connections')

@app.route('/')
def index():
    time.sleep(0.1)
    connections_counter.inc()
    return 'Hello, World!'

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
