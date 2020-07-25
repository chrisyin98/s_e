from flask import Flask, redirect, url_for, render_template, request, jsonify
from engine import *
import json
app = Flask(__name__)

@app.route("/")
def home():
  return render_template("start.html")

@app.route('/search', methods=['POST'])
def getResults():
  result = request.get_data(as_text=True)
  result_list = start(result)
  return json.dumps([ob.__dict__ for ob in result_list])

@app.route("/search/www.google.com") # need a place to redirect
def results_page():
  return render_template("results.html")


if __name__ == "__main__":
  app.run(debug=True)