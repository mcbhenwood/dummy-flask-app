import os

import requests
from flask import Flask, Response

app = Flask(__name__)


@app.route("/")
def hello():
    return Response("Hello! (version 2)")


@app.route("/retrieve_other_service_content")
def retrieve_other_service_content():
    foreign_service_url = os.getenv("FOREIGN_SERVICE_URL", None)
    if not foreign_service_url:
        return Response("Service is not configure with FOREIGN_SERVICE_URL :(")
    r = requests.get(foreign_service_url)
    return Response(' Foreign service said "{}"'.format(r.text))
