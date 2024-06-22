from flask import Flask, request, jsonify
import classifier
from dotenv import load_dotenv
load_dotenv()
import os

app = Flask(__name__)

predictor = classifier.Classifier()

@app.route("/classify", methods=["POST"])
def classify():
  req = request.get_json()

  if req['key'] != os.environ.get('SECRET_KEY'):
    return jsonify({"Not Authorized"}), 401

  imgDataURL = req['imgDataURL']

  processedImg = classifier.process_img(imgDataURL)

  prediction = predictor.classify(processedImg, 5)
  print(prediction)

  return jsonify({"predictions": prediction})





  