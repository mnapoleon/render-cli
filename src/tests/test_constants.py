import responses
from renderctl.render_services import RENDER_API_BASE_URL

test_svc_1 = {
            "cursor": "eMHLdAJXBHZqcmhncDNqcW5sMHF1Z29n",
            "service": {
                "id": "srv-cc3vjrhgp3jqnl0xxxxx",
                "name": "render-service-name-1",
                "serviceDetails": {
                    "url": "https://render-service-name-1.onrender.com"
                }
            }
        }

test_svc_2 = {
            "cursor": "eMHLdAJXBHZqcmhncDNqcW5sMHF1Z29l",
            "service": {
                "id": "srv-cc3vjrhgp3jqnl0yyyy",
                "name": "render-service-name-2",
                "serviceDetails": {
                    "url": "https://render-service-name-1.onrender.com"
                }
            }
        }

test_svc_3 = {
            "cursor": "eMHLdAJXBHZqcmhncDNqcW5sMHF1Z29p",
            "service": {
                "id": "srv-cc3vjrhgp3jqnl0zzzz",
                "name": "render-service-name-3",
                "serviceDetails": {
                    "url": "https://render-service-name-3.onrender.com"
                }
            }
        }

test_services = [test_svc_1, test_svc_2, test_svc_3]

fetch_services_response = responses.Response(
    method="GET",
    url=RENDER_API_BASE_URL,
    json=test_services,
    status=200,
)

fetch_services_failed_with_401 = responses.Response(
    method="GET",
    url=RENDER_API_BASE_URL,
    status=401,
)

fetch_services_failed_with_406 = responses.Response(
    method="GET",
    url=RENDER_API_BASE_URL,
    status=406,
)

fetch_services_failed__with_429 = responses.Response(
    method="GET",
    url=RENDER_API_BASE_URL,
    status=429,
)

fetch_services_failed__with_500 = responses.Response(
    method="GET",
    url=RENDER_API_BASE_URL,
    status=500,
)

fetch_services_failed__with_503 = responses.Response(
    method="GET",
    url=RENDER_API_BASE_URL,
    status=503,
)

fetch_services_failed__with_402 = responses.Response(
    method="GET",
    url=RENDER_API_BASE_URL,
    status=402,
)

test_env_var_1 = {
        "envVar": {
            "key": "APP_VER",
            "value": "deadball-player-generator.pr41"
        },
        "cursor": "nRitXfSIHIp0a3BhNmdkdjMzYXVjOWcw"
    }

test_env_var_2 =  {
        "envVar": {
            "key": "APP_NAME",
            "value": "deadball-player-generator"
        },
        "cursor": "nRitXfSIHIp0a3BhNmdkdjMzYXVjOWZn"
    }

test_env_var_3 =  {
        "envVar": {
            "key": "PYTHON_VERSION",
            "value": "3.10.6"
        },
        "cursor": "nRitXfSIHIp0a3BhNmdkdjMzYXVjOWYw"
    }

test_env_var_4 = {
        "envVar": {
            "key": "TEST_ID",
            "value": "123456"
        },
        "cursor": "nRitXfSIHIpzaWhhNmdkdjMzYXViODhn"
    }

test_env_vars = [test_env_var_1, test_env_var_2, test_env_var_3, test_env_var_4]

retrieve_env_vars_response = responses.Response(
    method="GET",
    url=f"{RENDER_API_BASE_URL}/service-id/env-vars",
    json=test_env_vars,
    status=200,
)

retrieve_env_vars_failed_with_401 = responses.Response(
    method="GET",
    url=f"{RENDER_API_BASE_URL}/service-id/env-vars",
    status=401,
)
