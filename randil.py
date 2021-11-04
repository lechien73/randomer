from datetime import datetime
import json
import os

from flask import Flask
from flask_cors import CORS
from helpers.get_image import get_dilbert
from helpers.random_date import random_date


app = Flask(__name__)
cors = CORS(app, resources={r"/api*": {"origins": "*"}})


@app.route("/api")
def api():

    now = datetime.now()
    strip_to_get = random_date(now)

    return json.dumps(get_dilbert(strip_to_get)), 200, {"ContentType": "application/json"}


if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"), port=int(
        os.getenv("PORT", "5000")), debug=False)