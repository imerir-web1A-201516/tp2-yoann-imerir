import json
from flask import Flask, make_response, request
app = Flask(__name__)
products = ["Pear", "Apple"]
@app.route("/products/")
def products():
    resp = make_response(json.dumps(products), 200)
    resp.headers['Content-Type'] = 'application/json'
    return  resp
@app.route("/products/", methods=["POST"])
def products_add():
    global products
    prod = request.get_json()
    products.append(prod)
    resp = make_response("True", 201)
    resp.headers['Content-Type'] = 'application/json'
    resp.headers['Location'] = '/products/%d' % (len(products) - 1)
    return  resp
if __name__ == "__main__":
    app.run()
