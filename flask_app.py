
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/kontenübersicht")
def kontenübersicht():
    return render_template("kontenübersicht.html")

@app.route("/informationen_berechtigungen")
def informationen_berechtigungen():
    return render_template("informationen_berechtigungen.html")

@app.route("/in_arbeit")
def in_arbeit():
    return render_template("in_arbeit.html")

if __name__ == '__main__':
    app.run()