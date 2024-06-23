from flask import Flask, render_template
from models import portfolio
#Server imports
from gevent.pywsgi import WSGIServer
import os

if os.name != "nt":
    os.chdir(os.path.dirname(_file_))

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return render_template('index.html', portfolio = portfolio())

if __name__ == "__main__":
    http_server = WSGIServer(("0.0.0.0", 2003), app)
    http_server.serve_forever()
    #app.run(host="0.0.0.0", debug=True)