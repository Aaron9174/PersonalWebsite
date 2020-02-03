from flask import Flask, request, escape
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class health(Resource):
    def get(self):
        return "The server is healthy."

api.add_resource(health, "/home")

@app.route("/")
def hello():
    name = request.args.get("name", "World")
    return f"Hello, {escape(name)}!"

