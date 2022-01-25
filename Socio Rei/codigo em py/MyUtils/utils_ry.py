import requests

def checkNet():
    try:
        requests.get('https://www.google.com/')
    except requests.exceptions.ConnectionError:
        return False
    else:
        return True
