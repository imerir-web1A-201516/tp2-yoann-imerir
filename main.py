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
def products():
  

@app.route("/")
def hello():
  return "Hello the world!"

if __name__ == "__main__":
  app.debug=True
  app.run()
