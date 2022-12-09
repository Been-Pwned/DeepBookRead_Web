from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def mainpage():
    return render_template("index.html")

@app.route("allbooks")
def allbooks():
    return render_template("comingsoon.html")

if '__main__' == __name__:
    app.run()
