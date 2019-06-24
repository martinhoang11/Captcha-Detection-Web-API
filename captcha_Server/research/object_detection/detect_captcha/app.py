from flask import Flask, request
import requests
from flask_restful import Resource, Api
from api import detection


app = Flask(__name__)
api = Api(app)
app.register_blueprint(detection)

if __name__ == '__main__':
    app.run(debug=True)
