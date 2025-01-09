import requests

URL = "https://192.168.10.61/api/jsonrpc"


def login(username: str, password: str) -> str:

    payload = {
    "id": 0,
    "jsonrpc": "2.0",
    "method": "Api.Login",
    "params": {
        "user": username,
        "password": password
    }
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(URL, json=payload, headers=headers, verify=False)
        response.raise_for_status()
        
        response_json = response.json()
        
        token = response_json.get("result", {}).get("token")
        return token

    except requests.exceptions.RequestException as e:
        print("Error:", e)

