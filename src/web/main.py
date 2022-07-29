from flask import Flask, request, render_template, redirect, Response, make_response, jsonify
import json
import os
from . import composer_api
from ..config import *

app = Flask(__name__)

app.logger.info(f"{COMPOSER_MODULE=}")


@app.route("/hello")
def hello_world():
    return "<p> hello World</p>"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/vuldetail/<int:vulid>", methods=["GET"])
def get_vuldetail(vulid):

    return render_template("vuldetail.jinja2", vulid=vulid)


# Get the json format list of available vulhub
@app.route("/list", methods=["GET"])
def list_vuls():
    dirs = [("./vulnerability", 0)]
    output = []

    for d, layer in dirs:
        if not os.path.isdir(d):
            continue
        for subd in os.listdir(d):
            dirs.append((f"{d}/{subd}", layer + 1))
        # TODO maybe not layer 2?
        if layer == 3:
            output.append(d)

    return json.dumps(output)


# get list of running/upping vultargets
@app.route("/vultargets", methods=["GET"])
def get_vultargets():
    return json.dumps(composer_api.get_compose_status())
    


# Create vultarget
@app.route("/vultarget", methods=["POST", "DELETE"])
def manage_vultarget():
    data = request.get_json()
    app.logger.info(request.data)
    app.logger.debug(data["vultarget"])
    if request.method == "POST":
        composer_api.send_compose_up(data["vultarget"])
    if request.method == "DELETE":
        composer_api.send_compose_down(data["vultarget"])
    return "Ok"


@app.errorhandler(404)
def page_not_found(e):
    return_result = {
        "code": 404,
        "Success": False,
        "Message": "The website is not available currently",
    }
    return jsonify(return_result), 404


@app.errorhandler(403)
def forbidden(e):
    return_result = {
        "code": 403,
        "Success": False,
        "Message": "The website is not available currently",
    }
    return jsonify(return_result), 403


if __name__ == "__main__":
    app.run(host="::", port=5000)
