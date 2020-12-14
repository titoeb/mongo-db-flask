from flask import Flask
from flask_restful import Api, Resource
from pymongo import MongoClient

# Set-up App
app = Flask(__name__)
api = Api(app)

# Initiallize db connection
client = MongoClient("mongodb://mongo-db:27017")
db = client.aNewDB
# Select the UserNum collection
UserNum = db["UserNum"]
# Initiallize the number of user in the website as 0.
UserNum.insert({
    "number_of_users": 0
})

class Visit(Resource):
    def get(self):
        previous_number = UserNum.find({})[0]["number_of_users"]
        current_number = previous_number + 1
        UserNum.update({}, {"$set":{"number_of_users": current_number}})
        return f"Hello user {current_number}"

api.add_resource(Visit, "/visit")

if __name__ == "__main__":
    	app.run(debug=True)
