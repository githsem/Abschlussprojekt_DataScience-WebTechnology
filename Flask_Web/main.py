from flask import Flask, render_template, request
import TeamITea

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/vorhersage')
def my_form():
    return render_template('vorhersage.html')

@app.route('/vorhersage', methods=['POST'])
def my_form_post():
    text = request.form['text']
    result = TeamITea.vorhersage(text) 
    return render_template('vorhersage.html',result=result[0])

@app.route("/uberuns")
def uberuns():
    return render_template("uberuns.html")   
   
  

if __name__ == "__main__":
    app.run(debug=True)