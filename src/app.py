from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return "Hello World from inside a docker container that is hosted in docker-compoes."

if __name__ == "__main__":
    	app.run(debug=True)
