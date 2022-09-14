import requests
from requests import HTTPError
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
        if response.status_code == 200:
            try:
                response.raise_for_status()
                return response.json()
            except HTTPError as exc:
                print(f"{exc.status_code} - Error")
                raise SystemExit(exc)


def fetch_services(limit=20, cursor=None):
    cursor_query_param = f"&cursor={cursor}" if cursor is not None else ""
    url = f"{RENDER_API_BASE_URL}?limit={limit}{cursor_query_param}"
    with requests.get(url, headers=create_headers()) as response:
        return response.json()


def deploy_service(service_name):
    url = f"{RENDER_API_BASE_URL}/{service_name}/deploys"
    with requests.post(url, headers=create_headers(is_post=True)) as response:
        return response.json()


def find_service_by_name(service_name: str):
    data = fetch_services(limit=50)
    found = False
    resulting_service = None
    cursor = None
    while True:
        for svc_listing in data:
            service = svc_listing['service']
            cursor = svc_listing['cursor']
            if service['name'] == service_name:
                resulting_service = svc_listing
                found = True
                break
        if found:
            break
        data = fetch_services(cursor=cursor)
        if len(data) == 0:
            break
    return resulting_service


def handle_errors(status_code):
    if status_code == 401:
        print("401 - Unauthorized")
    elif status_code == 406:
        print('406 - request error')
    elif status_code == 429:
        print('429 - Exceeded service limit')
    elif status_code == 500 or status_code == 503:
        print(f"{status_code} - Render service unavailable")
    else:
        print(f"{status_code} - unexpected error")