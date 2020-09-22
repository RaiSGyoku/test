from flask import Flask
from flask_restful import Api
from model.app import HelloWorld

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0',port=5000) # adjustable to any port and any setted ip