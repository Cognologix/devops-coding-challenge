from flask import  Flask, jsonify, request
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)
class Hello(Resource):
    def get(self):
        return jsonify({'message' : 'hello cognologix'})
    def post(self):
        data = request.get_json()
        return jsonify({'data': data}),201
class Strngr(Resource):
    def get(self):
        return jsonify({'message':'hello stranger'})
api.add_resource(Hello,'/cognologix')
api.add_resource(Strngr, '/')

if __name__ == '__main__':
    app.run(port=9097)
