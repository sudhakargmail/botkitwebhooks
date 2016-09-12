'''
Created on May 18, 2016

@author: Sudhakar
'''

from flask import Flask
application = Flask(__name__)

from enums import MessagingProviders
from amadeus import flights_low_fare_search, amadeus_results_to_facebook
from expedia import get_ean_tags_from_webhook_input, expedia_search_request_to_facebook



@application.route("/")
def hello():
    return "Hello! The Python is all set. You can run the webhooks now"


if __name__ == "__main__":
    application.run()