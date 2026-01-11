import requests
import os
from dotenv import load_dotenv

load_dotenv()

DIRECTUS_URL = os.getenv("DIRECTUS_URL")
DIRECTUS_TOKEN = os.getenv("DIRECTUS_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {DIRECTUS_TOKEN}",
    "Content-Type": "application/json"
}

def create_experiment_directus(data):
    url = f"{DIRECTUS_URL}/items/experiments"
    response = requests.post(url, json=data, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def list_experiments_directus():
    url = f"{DIRECTUS_URL}/items/experiments"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_experiment_by_id_directus(exp_id):
    url = f"{DIRECTUS_URL}/items/experiments/{exp_id}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()
print("DIRECTUS_TOKEN:", DIRECTUS_TOKEN)
