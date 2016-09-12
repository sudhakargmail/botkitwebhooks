'''
Created on May 18, 2016

@author: Sudhakar
'''

from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello! The Python is all set. You can run the webhooks now"


if __name__ == "__main__":
    application.run()