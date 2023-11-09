from flask import Flask, render_template

app = Flask(__name__)

# To run: first execute '. .venv/bin/activate'
# Next, run 'flask --app demo run'

@app.route("/")
def home():
    return render_template("index.html")