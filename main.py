from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from model.app import HelloWorld, getList

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(HelloWorld, '/')
api.add_resource(getList, '/app/v1/getall')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0',port=5000) # adjustable to any port and any setted ip