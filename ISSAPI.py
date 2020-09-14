import requests
import json

response = requests.get('https://api.wheretheiss.at/v1/satellites/25544')
Jsonresponse = response.json()


if response.status_code == 200:
    print ("Everything is ok and works fine. ")
    print (response.status_code)
else:
    print("There was an issue that occoured when calling thew API. ")
    print(response.status_code)

UsrQuestion = input("What is your question? ")
print(Jsonresponse[UsrQuestion])


input()