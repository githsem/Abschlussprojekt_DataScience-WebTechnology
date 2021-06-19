from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    
    article = dict()
    article['title']='TEST'
    article['body']='TEST222'
    return render_template("index.html",article=article)

@app.route("/about")
def about():
    return "About"


if __name__ == "__main__":
    app.run(debug=True)