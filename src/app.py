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

# Helper functions
def verify_user(username:str, password: str) -> bool:
    hashed_pw = users.find({
        "Username": username
        })[0]["Password"]

    return bcrypt.hashpw(password.encode("utf8"), hashed_pw) == hashed_pw

def count_tokens(username:str) -> bool:
    return users.find({
        "Username": username
        })[0]["Tokens"]

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
            "Tokens": 5,
            "Sentence": ""
        })
        retJson = {
                "status": 200,
                "msg": "User was sucessfully created"
        }
        return jsonify(retJson)

class Store(Resource):
    def post(self):
        postedData = request.get_json()
        # Parse input data.
        username = postedData["username"]
        password = postedData["password"]
        sentence = postedData["sentence"]

        # Verify username password combination
        correct_pw = verify_user(username, password)
        if not correct_pw:
            return jsonify({
                "status": 302,
                "msg": "Username and password don't match"})
        # Verify user has enough tokens
        number_tokens = count_tokens(username)
        if number_tokens <= 0:
            return(jsonify({
                    "status": 301,
                    "msg": "You don't have enough tokens!"
                }))

        # Store sentence and return sucess.
        users.update({"Username": username}, {"$set": {"Sentence": sentence, "Tokens": number_tokens-1}})
        return(jsonify({
            "status": 200,
            "msg": "Sentence was stored succesfully"
             }))

class Get(Resource):
    def get(self):
        postedData = request.get_json()
        
        username = postedData["username"]
        password = postedData["password"]
        
        # Verify username password combination
        correct_pw = verify_user(username, password)
        if not correct_pw:
            return jsonify({
                "status": 302,
                "msg": "Username and password don't match"})
        # Verify user has enough tokens
        number_tokens = count_tokens(username)
        if number_tokens <= 0:
            return(jsonify({
                    "status": 301,
                    "msg": "You don't have enough tokens!"
                }))

        sentence = users.find({
            "Username": username})[0]["Sentence"]

        return(jsonify({"status": 200, "msg": sentence}))


api.add_resource(Register, "/register")
api.add_resource(Store, "/store")
api.add_resource(Get, "/get")

if __name__ == "__main__":
    	app.run(debug=True)
