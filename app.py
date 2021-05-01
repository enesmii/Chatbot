import aiml
from flask import Flask, render_template
import os

kernel = aiml.Kernel()
kernel.learn("start.xml")
kernel.respond("PMB")
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/<query>')
def api(query):
    print(kernel.respond(query))
    return kernel.respond(query)
    # return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)