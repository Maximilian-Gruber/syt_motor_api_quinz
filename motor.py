import requests

URL = "https://192.168.10.61/api/jsonrpc"

def browseMotor(token: str):
    payload = {
        "jsonrpc": "2.0",
        "id": 4,
        "method": "PlcProgram.Browse",
            "params": {
            "var": "\"Motor\"",
            "mode": "children"
        }
    }

    headers = {
        "Content-Type": "application/json",
        "X-Auth-token": f"{token}"
    }


    try:
        response = requests.post(URL, json=payload, headers=headers, verify=False)
        response.raise_for_status()
        
        response_json = response.json()
        return response_json
    
    except requests.exceptions.RequestException as e:
        print("Error:", e)


def startMotor(token: str):
    payload = {
        "jsonrpc": "2.0",
        "method": "PlcProgram.Write",
        "id": 1,
        "params": {
            "var": "\"Motor\".ein",
            "value": True
        }
    }

    headers = {
        "Content-Type": "application/json",
        "X-Auth-token": f"{token}"
    }


    try:
        response = requests.post(URL, json=payload, headers=headers, verify=False)
        response.raise_for_status()
        
        response_json = response.json()
        return response_json
    
    except requests.exceptions.RequestException as e:
        print("Error:", e)



def stopMotor(token: str):
    payload = {
        "jsonrpc": "2.0",
        "method": "PlcProgram.Write",
        "id": 1,
        "params": {
            "var": "\"Motor\".ein",
            "value": False
        }
    }

    headers = {
        "Content-Type": "application/json",
        "X-Auth-token": f"{token}"
    }


    try:
        response = requests.post(URL, json=payload, headers=headers, verify=False)
        response.raise_for_status()
        
        response_json = response.json()
        return response_json
    
    except requests.exceptions.RequestException as e:
        print("Error:", e)


def readData(token: str, type: str):
    payload = {
        "jsonrpc": "2.0",
        "method": "PlcProgram.Read",
        "id": 1,
        "params": {
            "var": type
        }
    }

    headers = {
        "Content-Type": "application/json",
        "X-Auth-token": f"{token}"
    }

    try:
        response = requests.post(URL, json=payload, headers=headers, verify=False)
        response.raise_for_status()
        
        response_json = response.json()
        return response_json
    
    except requests.exceptions.RequestException as e:
        print("Error:", e)