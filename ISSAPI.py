import requests

response = requests.get('https://api.wheretheiss.at/v1/satellites/25544')

print(response.status_code)
print(response.json())