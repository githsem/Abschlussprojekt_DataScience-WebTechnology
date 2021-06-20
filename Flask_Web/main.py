from flask import Flask, render_template
import TeamITea

app = Flask(__name__)

@app.route("/")
def index():
    result = TeamITea.vorhersage('schlect')
    return render_template("index.html",result=result)

@app.route("/about")
def about():
    return "About"


if __name__ == "__main__":
    app.run(debug=True)