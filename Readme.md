# Flask template

## How to use
This is my Flask template that I use to build flask based web-services. It has a development and a production set-up. To develop the web-service start-up the environment with `docker-compose up`. Then you can develop the code locally on your computer. To add packages to the environment, simply add them to the `requirements.txt`-file and rebuild the image with `docker-compose up --build`. The `Dockerfile` then can be adapted to production and copies the current state of the flask-app and executes it. 

# Resource Table
In the following table you should document the resources of your rest-api to make it easier to understand:
| Resource | Method | Path | Used to | Parameters | error-codes |
| --- | --- | --- | --- | --- | --- |
| Register a user | POST | /register | username:str, password:str | 200 OK | 
| Store a sentence | POST | /store | username:str, password:str, sentence:str | 200 OK, 301 Out of Tokens, 302 Invalid Username Password Combination |
| Retrive a sentence | POST | /get | username:str, password: str | 200 OK, 301 Out of Tokens, 302 Invalid Username Password Combination |

Happy Hacking!
