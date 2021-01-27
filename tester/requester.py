import requests
import time
import os

host = os.environ.get("FLASK_HOST", default="localhost")
print(host)
while True:
    x = requests.get(f"http://{host}:5000/")
    assert x.status_code == 200
    print(x.text)
    time.sleep(1)
