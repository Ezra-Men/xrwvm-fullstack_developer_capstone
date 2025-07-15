import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv('sentiment_analyzer_url', default="http://localhost:5050/")

def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params += f"{key}={value}&"
    params = params.rstrip('&')
    request_url = f"{backend_url}{endpoint}"
    if params:
        request_url += f"?{params}"
    print(f"GET from {request_url}")
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return {"error": "Request failed", "details": str(e)}

def analyze_review_sentiments(text):
    try:
        request_url = sentiment_analyzer_url + "analyze/" + text
        print(f"Analyzing sentiment for: {text}")
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Sentiment analysis error: {e}")
        return {"sentiment": "neutral", "error": str(e)}

def post_review(data_dict):
    try:
        request_url = backend_url + "insert_review"
        print(f"Posting review to: {request_url}")
        response = requests.post(request_url, json=data_dict)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error posting review: {e}")
        return {"error": "Post failed", "details": str(e)}
