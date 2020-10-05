#!flask/bin/python
from flask import Flask, jsonify
import subprocess
import sys

app = Flask(__name__)

@app.route('/pronouns', methods=['GET'])
def twitter_count():
    data=subprocess.check_output(["python3","calling_celery.py"])
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 50070, debug=True)