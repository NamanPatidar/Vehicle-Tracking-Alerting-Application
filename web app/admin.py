from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/remove")
def remove():
    return render_template('remove.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/add")
def add():
    return render_template('add.html')


app.run(debug=True)
