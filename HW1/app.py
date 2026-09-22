from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/profile")
def profile():
    hobbys = ["climbing", "watching movie", "playing game"]
    return render_template("profile.html", hobbys = hobbys)

@app.route("/greet/<name>")
def greet(name):
    return render_template("greet.html", name=name)

