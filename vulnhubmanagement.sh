#!/bin/bash

workdir="/etc/vulnhubmanagement"

. ./venv/bin/activate

#python server.py
gunicorn --bind [::]:80 vulnhubmanagement:app
#gunicorn --certfile=server.crt --keyfile=server.key --bind [::]:443 server:app
