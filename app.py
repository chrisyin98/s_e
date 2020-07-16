from flask import Flask, redirect, url_for, render_template, request
from engine import *
app = Flask(__name__)

@app.route("/")
def home():
  return render_template("start.html")

@app.route('/search', methods=['POST'])
def getResults():
  print(request)

if __name__ == "__main__":
  app.run(debug=True)