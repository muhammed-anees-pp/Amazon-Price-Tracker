import os
import requests
from dotenv import load_dotenv
load_dotenv()


# SEND REQUEST TO OXYLABS API
def post_query(payload):
    username = os.getenv("OXYLABS_USERNAME")
    password = os.getenv("OXYLABS_PASSWORD")

    response = requests.post(os.getenv("OXYLABS_BASE_URL"), auth=(username, password), json=payload)
    response.raise_for_status()
    response_json = response.json()
    return response_json


