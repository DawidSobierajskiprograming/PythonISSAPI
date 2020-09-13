import requests
import json

response = requests.get('https://api.wheretheiss.at/v1/satellites')

print(response.status_code)

def jprint(obj):
    text = json.dumps(obj,sort_keys=True, indent=4)
    print(text)

jprint(response.json())