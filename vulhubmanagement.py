import os
import json

from flask import Flask,request,redirect,Response,make_response

app = Flask(__name__)

@app.route('/',methods=['GET'])
def alive():
    return "true"

@app.route('/list',methods=['GET'])
def listdir(dirname = 'vulnerability', layer = 0):
    output = []
    for a in os.listdir(dirname):
        if layer < 2:
            output + json.loads(listdir(dirname = dirname + '/' + a))
        else:
            output.append(dirname + '/' + a)
    return json.dumps(output)

@app.route('/start',methods=['POST'])
def start():
    data = json.loads(request.get_data().decode())



@app.errorhandler(404)
def page_not_found(e):
    return_result = {'code': 404, 'Success': False,
                     "Message": "The website is not available currently"}
    return jsonify(return_result), 404


@app.errorhandler(403)
def forbidden(e):
    return_result = {'code': 403, 'Success': False,
                     "Message": "The website is not available currently"}
    return jsonify(return_result), 403


if __name__ == "__main__":
    app.run(host="::",port=8000)

