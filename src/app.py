from flask import Flask, jsonify
import bcrypt
from flask_restful import Api, Resource, request
from pymongo import MongoClient

# Set-up App
app = Flask(__name__)
api = Api(app)

# Initiallize db connection
client = MongoClient("mongodb://mongo-db:27017")
db = client.SentencesDatabase
users = db["users"]

class Register(Resource):
    def post(self):
        postedData = request.get_json()

        # Parse inputs
        username = postedData["username"]
        password = postedData["password"]
        # Hash user password
        hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        # Store the user data into the database.
        users.insert({
            "Username": username,
            "Password": hashed_password,
            "sentence": ""
        })
        retJson = {
                "status": 200,
                "msg": "User was sucessfully created"
        }
        return jsonify(retJson)

api.add_resource(Register, "/register")

if __name__ == "__main__":
    	app.run(debug=True)
