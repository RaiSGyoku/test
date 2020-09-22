from flask_restful import Resource
from flask import jsonify, request
import json
import csv 
from datetime import datetime


# read file #set as database for the mean time
with open('data/data.json', 'r') as myfile:
    data=myfile.read()

obj = json.loads(data)

class HelloWorld(Resource):
  def get(self):
    return "Hello Dear Developer please add the following on the url to test the api" + " 1. /app/v1/getall " + " 2. /app/v1/create "+ " 3. /app/v1/delete "+ "4. /app/v1/update "


#view
class getList(Resource):
  def get(self):
    return jsonify(obj)
#not useful for the project    def sortFunction(value):
      #return value["Date"]
#not useful for the project      return  datetime.strptime(value['Date'], '%B %d, %Y')

    #sortedItem = sorted(obj, key=sortFunction)
#not useful for the project    sorted_date = sorted(obj, key=sortFunction)
    
#not useful for the project    return jsonify(sorted_date) #  sortedItem  #jsonify(sorted(obj, key='Date'))

#create
class addList(Resource):
  def post(self):
    # Get item from the POST body
    req_data = request.get_json()
    obj.append(req_data)
    #obj.update(req_data)
    with open('data.json', 'w') as outfile: #animelist #webinar
      json.dump(obj, outfile, indent = 4)     
    myfile.close()
    return jsonify(req_data)