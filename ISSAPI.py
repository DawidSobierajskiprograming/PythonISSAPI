import tkinter
from tkinter import *
from tkinter import messagebox
import requests
import json


url = 'https://api.wheretheiss.at/v1{}'

IsItUp = requests.get(url.format('/satellites/25544'))


if IsItUp.status_code == 200:
    print ("Everything is ok and works fine. ")
    print (IsItUp.status_code)
else:
    print("There was an issue that occoured when calling thew API. ")
    print(IsItUp.status_code)

def getaltitude():
    getdataURL = requests.get(url.format('/satellites/25544'))
    jresponse = getdataURL.json()
    altitudestr = str(jresponse['altitude'])
    return altitudestr

def getvelocity():
    getdataURL = requests.get(url.format('/satellites/25544'))
    jresponse = getdataURL.json()
    velocitystr = str(jresponse['velocity'])
    return velocitystr

def getlatitude():
    getdataURL = requests.get(url.format('/satellites/25544'))
    jresponse = getdataURL.json()
    latitudestr = str(jresponse['latitude'])
    return latitudestr

def getlongitude():
    getdataURL = requests.get(url.format('/satellites/25544'))
    jresponse = getdataURL.json()
    longitudestr = str(jresponse['longitude'])
    return longitudestr

def getcountrycode():
    getdataURL = requests.get(url.format('/coordinates/'+ getaltitude() +','+getlongitude()))
    jresponse = getdataURL.json()
    countrycode = jresponse['country_code']
    return countrycode