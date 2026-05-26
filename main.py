from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/clicked")
def clicked():
    return f"<p>Clicked me :)</p>"