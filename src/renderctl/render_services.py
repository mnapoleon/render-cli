import requests
import os


RENDER_API_BASE_URL = 'https://api.render.com/v1/services'


def get_bearer_token():
    return os.getenv('RENDER_TOKEN')


def retrieve_env_from_render(service_name):
    url = f"{RENDER_API_BASE_URL}/{service_name}/env-vars?limit=20"
    bearer = f"Bearer {get_bearer_token()}"
    headers = {
        "Accept": "application/json",
        "Authorization": bearer
    }

    response = requests.get(url, headers=headers)
    return response.text


def fetch_services():
    url = f"{RENDER_API_BASE_URL}?limit=20"
    bearer = f"Bearer {get_bearer_token()}"
    headers = {
        "Accept": "application/json",
        "Authorization": bearer
    }
    with requests.get(url, headers=headers) as response:
        return response.json()


def deploy_service(service_name):
    url = f"{RENDER_API_BASE_URL}/{service_name}/deploys"
    bearer = f"Bearer {get_bearer_token()}"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": bearer
    }
    with requests.post(url, headers=headers) as response:
        return response.json()