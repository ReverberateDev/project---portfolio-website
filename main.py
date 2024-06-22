from flask import Flask, render_template
from models import portfolio

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', portfolio = portfolio())

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)