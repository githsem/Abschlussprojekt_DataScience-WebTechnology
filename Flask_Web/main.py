from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    nummer = 10
    return render_template("index.html",nummer=nummer)

@app.route("/about")
def about():
    return "About"


if __name__ == "__main__":
    app.run(debug=True)