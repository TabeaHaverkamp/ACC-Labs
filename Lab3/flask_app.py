#!flask/bin/python
from flask import Flask, jsonify
#from flas_restful import Api, Resource, reqparse
import subprocess
import sys

app = Flask(__name__)


@app.route('/pronouns', methods=['GET'])
def twitter_count():
    data=subprocess.check_output(["python3","calling_celery.py"])
    return data

if __name__ == '__main__':
    
    app.run(host='0.0.0.0',debug=True)