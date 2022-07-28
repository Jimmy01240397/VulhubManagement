#!/bin/bash

workdir="/etc/vulhubmanagement"

. ./venv/bin/activate

#python server.py
gunicorn --bind [::]:80 vulhubmanagement:app
#gunicorn --certfile=server.crt --keyfile=server.key --bind [::]:443 server:app
