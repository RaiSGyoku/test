from flask_restful import Resource
from flask import jsonify, request
import json




class HelloWorld(Resource):
  def get(self):
    return "Hello Dear Developer please add the following on the url to test the api" + " 1. /todo/getall " + " 2. /todo/create "+ " 3. /todo/delete "+ "4. /todo/update "
