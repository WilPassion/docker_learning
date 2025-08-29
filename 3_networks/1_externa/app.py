import flask
from flask import request, json, jsonify
import requests

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET"]) # URL "/" (raiz do site) 
# e usar o método HTTP GET, execute a função:
def index():
    data = requests.get("https://randomuser.me/api") #requisição GET para a API
    return data.json() #retorna o resultado da API em JSON

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
    
# 1) Built image: docker build -t flaskexterna .
# 2) Run container: docker run -d -p 5000:5000 --name flask_externo_container flaskexterna