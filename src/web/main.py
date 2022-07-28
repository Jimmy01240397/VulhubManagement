from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/hello')
def hello_world():
  return '<p> hello World</p>'

@app.route('/')
def index():
  return 'Index of /\n\t/etc/shadow\n\t/etc/passwd'


@app.route('/vuldetail/<int:vulid>', methods=['GET'])
def get_vuldetail(vulid):
  
  return render_template('vuldetail.jinja2', vulid=vulid)

@app.route('/vultargets', methods=['GET'])
def get_vultargets():
  pass

@app.route('/vultarget', methods=['POST'])
def create_vultarget():
  pass
