import os

import requests
from flask import Flask, Response, request

app = Flask(__name__)


@app.route("/")
def hello():
    http_host = request.headers["host"]
    return Response(
        "Hello! (version 3) - I am serving content for HTTP host '{}'".format(http_host)
    )


@app.route("/retrieve_other_service_content")
def retrieve_other_service_content():
    foreign_service_url = os.getenv("FOREIGN_SERVICE_URL", None)
    if not foreign_service_url:
        return Response("Service is not configure with FOREIGN_SERVICE_URL :(")
    r = requests.get(foreign_service_url)
    return Response(' Foreign service said "{}"'.format(r.text))
