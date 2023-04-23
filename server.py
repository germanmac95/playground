from flask import Flask, render_template

app = Flask(__name__)

@app.route("/one")
def first():
    return render_template("index.html",num=3,color="blue")

@app.route("/<color>/<number>/")
def index(color,number):
    return render_template("index.html", color=color, num=int(number))


if __name__ == "__main__":
    app.run(debug=True)