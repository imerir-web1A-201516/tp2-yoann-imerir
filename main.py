# -*- coding: utf-8 -*-
import json
from flask import Flask
app = Flask(__name__)

students = [
  {"name": "John", "grades": [{"topic": "French", "mark": 12}, {"topic": "Math", "mark": 16}]},
  {"name": "Jane", "grades": [{"topic": "French", "mark": 18}, {"topic": "Math", "mark": 9}]},
  {"name": "Toto", "grades": [{"topic": "French", "mark": 8}, {"topic": "Math", "mark": 5}]}
]
@app.route("/eleves/")
def get_liste_eleves():
	eleves = json.loads(students)
	liste_eleves = eleves['name']
	

@app.route("/")
def hello():
  return  '<html><head><title>Bienvenue</title></head><body>Découvrez <a href="/products/">nos produits</a>.<br> <a href="/eleves/">Eleves</a></body></html>'

@app.route("/products/")
def products():
    return  '<html><head>    <title>Products</title></head><body>    <ul><li>Pear</li><li>Apple</li><li>…</li></ul></body></html>'
if __name__ == "__main__":
    app.run()
