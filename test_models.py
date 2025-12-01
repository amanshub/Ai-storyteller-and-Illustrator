import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("HUGGINGFACE_API_TOKEN")
headers = {"Authorization": f"Bearer {api_key}"}

models = [
    "runwayml/stable-diffusion-v1-5",
    "CompVis/stable-diffusion-v1-4"
]

endpoints = [
    "https://router.huggingface.co/models",
    "https://api-inference.huggingface.co/models"
]

print(f"Testing key: {api_key[:5]}...")

for model in models:
    for base_url in endpoints:
        url = f"{base_url}/{model}"
        try:
            print(f"Testing {url}...")
            response = requests.post(url, headers=headers, json={"inputs": "cat"})
            print(f"STATUS: {response.status_code}")
            if response.status_code == 200:
                print(">>> SUCCESS! <<<")
            else:
                print(f"FAIL: {response.text[:50]}")
        except Exception as e:
            print(f"ERR: {e}")
        print("-" * 20)
