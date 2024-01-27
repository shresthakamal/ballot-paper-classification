""" test """

import flask
from flask import jsonify, render_template, request
import classifier

app = flask.Flask(__name__, static_url_path="/static/")
app.config["DEBUG"] = False


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/api/v1/predict", methods=["POST"])
def predict():

    payload = request.get_json()
    prediction, pos, neg = classifier.predict(data=payload["data"])
    return jsonify({"result": str(prediction[0]), "post": pos, "neg": neg})


app.run(host="0.0.0.0", port=8000)
