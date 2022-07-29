import json
import os
import sys
import re
from flask import (
    Flask,
    request,
    render_template,
    redirect,
    Response,
    make_response,
    jsonify,
    send_file,
    abort,
)
import markdown
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


@app.route("/upload")
def upload():
    return render_template("upload.html")


@app.route("/vuldetail/vulndata/<path:vulid>", methods=["GET"])
def get_vulndata(vulid):
    return send_file("/app/vulnerability/" + vulid)


@app.route("/vuldetail/<path:vulid>", methods=["GET"])
def get_vuldetail(vulid):
    path = request.args.get("path", "")
    readme = ""
    docker = ""
    if path == "" or not os.path.isdir(f"vulnerability/{path}"):
        abort(404)
    if os.path.isfile(f"vulnerability/{path}/README.md"):
        with open(f"vulnerability/{path}/README.md") as f:
            readme = f.read()
            changeimg = re.findall(r"(\!\[\]\((.*)\))", readme)
            for a in changeimg:
                if os.path.isfile(f"vulnerability/{path}/{a[1]}"):
                    readme = readme.replace(a[0], f"![](vulndata/{path}/{a[1]})")
            readme = markdown.markdown(readme, extensions=["tables", "fenced_code"])
    if os.path.isfile(f"vulnerability/{path}/docker-compose.yml"):
        with open(f"vulnerability/{path}/docker-compose.yml") as f:
            docker = f"``` yaml\n{f.read()}\n```"
            docker = markdown.markdown(docker, extensions=["tables", "fenced_code"])
    return render_template(
        "vuldetail.jinja2",
        vulid=vulid,
        detail=readme,
        docker_compose=docker,
        vul_path=path,
    )


@app.route("/jail/network/<name>", methods=["POST"])
def connect_jail_network(name):

    composer_api.send_connect_network(name)
    return {"msg": f"try connect to {name} network"}


# Get the json format list of available vulhub
@app.route("/list", methods=["GET"])
def list_vuls():
    dirs = [("", 0)]
    output = []

    for d, layer in dirs:
        if not os.path.isdir("vulnerability/" + d):
            continue
        for subd in os.listdir("vulnerability/" + d):
            if subd[0] != "." and subd != "base":
                dirs.append((f"{d}/{subd}", layer + 1))
        # TODO maybe not layer 2?
        if layer == 3:
            output.append(d.strip("/"))

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
