# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


# def get_request(endpoint, **kwargs):
def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params+key+"="+value+"&"
    if params != "":
        request_url = backend_url+endpoint+"?"+params
    else:
        request_url = backend_url+endpoint

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except requests.exceptions.RequestException:
        # If any error occurs
        print("Network exception occurred")

# Add code for get requests to back end


# def analyze_review_sentiments(text):
# request_url = sentiment_analyzer_url+"analyze/"+text
# Add code for retrieving sentiments
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"/analyze/"+text
    print("Request URL is {}".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        print("Response is {}".format(response.json()))

        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")

# def post_review(data_dict):
# Add code for posting review


def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException:
        print("Network exception occurred")
