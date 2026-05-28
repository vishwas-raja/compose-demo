import os
from flask import Flask
import redis

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

@app.route("/")
def home():
    count = redis_client.incr("visits")
    return f"Hello from Flask + Redis! Visit count: {count}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
