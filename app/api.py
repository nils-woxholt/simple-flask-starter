# app/views.py

from . import app
from flask import request

# app 
import json

@app.route("/")
def root():
    return "Hello, from root! <p>you can call /health or post a 'temperature' value to the /score endpoint</p>"

@app.route("/health")
def hello():
    return {"api status": "Healthy"}

@app.route("/score", methods=['POST'])
def score():

    if request.content_type.startswith("application/json"):
        temperature = request.json['temperature']
    else:
        temperature = request.form.get("temperature", type=int)

    app.logger.debug(f"temp: {temperature}")

    # run model here
    if temperature > 26:
        anomaly = True
    else:
        anomaly = False
    
    return {'anomaly': anomaly}