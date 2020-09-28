#!flask/bin/python
from flask import Flask, jsonify
from flas_restful import Api, Resource, reqparse
import subprocess
import sys

app = Flask(__name__)


@app.route('/cowsay/api/v1.0/saysomething', methods=['GET'])
def cow_say():
    data=subprocess.check_output(["cowsay","Hello student"])
    return data

if __name__ == '__main__':
    
    app.run(host='0.0.0.0',debug=True)


@app.route('My/weird/path/to/HAPPINESS', methods=['GET'])
def twitter_count():
    data=subprocess.check_output(["cowsay","Hello student"])
    return data

if __name__ == '__main__':
    
    app.run(host='0.0.0.0',debug=True)