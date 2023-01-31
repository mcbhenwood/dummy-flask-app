#!/bin/sh -e
gunicorn -b 0.0.0.0:80 dummy:app
