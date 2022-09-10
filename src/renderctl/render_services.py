import requests
import os


RENDER_API_BASE_URL = 'https://api.render.com/v1/services'

APPLICATION_JSON = 'application/json'

def get_bearer_token():
    return os.getenv('RENDER_TOKEN')


def create_headers(is_post: bool = False):
    bearer = f"Bearer {get_bearer_token()}"
    headers = {
        "Accept": APPLICATION_JSON,
        "Authorization": bearer
    }
    if is_post:
        headers['Content-Type'] = APPLICATION_JSON
    return headers


def retrieve_env_from_render(service_name):
    url = f"{RENDER_API_BASE_URL}/{service_name}/env-vars?limit=20"
    with requests.get(url, headers=create_headers()) as response:
        return response.json()


def fetch_services():
    url = f"{RENDER_API_BASE_URL}?limit=20"
    with requests.get(url, headers=create_headers()) as response:
        return response.json()


def deploy_service(service_name):
    url = f"{RENDER_API_BASE_URL}/{service_name}/deploys"
    with requests.post(url, headers=create_headers(is_post=True)) as response:
        return response.json()