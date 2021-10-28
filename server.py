from flask import Flask, request
from flask_restful import Api
import json

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello_world():
    return { 
        "message": "Hello world"
    }

@app.route("/list")
def getList():
    with open('./ToDoList.json') as f:
        ToDoList = json.load(f)
    list = json.dumps(ToDoList)
    return list

@app.route("/update", methods=['POST'])
def addToList():
    list = request.data
    list = json.loads(list)
    with open('ToDoList.json', 'w') as f:
        list = json.dump(list, f)
    return {
        "message": "Updated" 
    }

if __name__ == '__main__':
    app.run(port=5000, debug=True)