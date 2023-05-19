from flask import Flask, render_template
from flask import request
import urllib.request, json

# Define app name
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])

def main():
    return render_template("index.html")

if __name__ =="__main__":
    app.run(debug=True)