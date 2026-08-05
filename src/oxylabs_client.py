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


# EXTRACT PRODUCT CONTENT FROM OXYLAB API RESPONSE
def extract_content(payload):
    if isinstance(payload, dict):
        if "results" in payload and isinstance(payload["results"], list) and payload["results"]:
            first = payload["results"][0]
            if isinstance(first, dict) and "content" in first:
                return first["content"] or {}
        if "content" in payload:
            return payload.get("content", {})

    return payload


# NORMALIZE PRODUCT DATA
def normalize_product(content):
    category_path = []
    if content.get("category_path"):
        category_path = [cat.strip() for cat in content["category_path"] if cat]

    return {
        "product_code": content.get("product_code"),
        "url": content.get("url"),
        "brand": content.get("brand"),
        "price": content.get("price"),
        "stock": content.get("stock"),
        "title": content.get("title"),
        "rating": content.get("rating"),
        "images": content.get("images", []),
        "categories": content.get("category", []) or content.get("categories", []),
        "category_path": category_path,
        "currency": content.get("currency"),
        "buybox": content.get("buybox", []),
        "product_overview": content.get("product_overview", [])
    }
