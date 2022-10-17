from flask import Flask
import numpy as np 

fastapi = Flask(__name__)

@fastapi.route('/',methods=['GET'])

def home():
    return "HELLO WORLD"

if __name__ =="__main__":
    fastapi.run(host='0.0.0.0', port=5000, debug=True)
