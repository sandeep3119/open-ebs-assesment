from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0)

app = Flask(__name__)


@app.route("/")
def hello():
  
    html = "<h1>Hiiii {name}</h1>" \
           "<h3><b>Hostname:</b> {hostname}</h3><br/>"
    return html.format(name=os.getenv('user-name'), hostname=socket.gethostname())


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
