import requests

response = requests.get('https://wheretheiss.at/w/developer')

print(response.status_code)