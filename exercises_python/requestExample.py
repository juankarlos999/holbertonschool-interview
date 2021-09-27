#!/usr/bin/python3

import json
from os import access
import requests


url_1 = "http://httpbin.org/post"
#url_2 = "https://maps.googleapis.com/maps/api/geocode/xml?address=cajica&key=AIzaSyA2z1JjPUiyTG7MuPpLGFCmWAycsRhdKK0"
url_2 = "https://maps.googleapis.com/maps/api/geocode/json"

def myGetMethod(url):
    myResponse = requests.get(url, params={"address":"bogota", "key":"AIzaSyA2z1JjPUiyTG7MuPpLGFCmWAycsRhdKK0"})
    print(myResponse.url)
    location =  myResponse.json()
    print(location["results"][0]["geometry"]["location"])

    if myResponse.status_code == 200:
        with open("ResponseUrl2.json", "wb") as file:
            file.write(myResponse.content)

def myPostMethod(url):
    headerContentType = {"Content-Type": "application/json", "access-token": "PutYourAccessToken"}
    payload = {"nombre":"Teo", "curso":"APIs", "nivel":"intermedio"}
    myResponse = requests.post(url, data=json.dumps(payload), headers=headerContentType)
    header = myResponse.headers
    headerToken = header["Server"]
    print(headerToken)
    print(myResponse.url, "\n")
    t = myResponse.content
    tt = json.loads(t)
    print(tt, "\n")
    #print(myResponse.text)


def myGetmethodFile():
    url = "https://pulpfictioncine.com/download/multimedia.normal.8239579a3a783434.73706f6e6765626f625f6e6f726d616c2e6a7067.jpg"

    myRequest = requests.get(url, stream=True)

    with open("Bob.jpg", "wb") as file:

        for load in myRequest.iter_content():
            file.write(load)
    myRequest.close()



if __name__ == '__main__':

   # myGetMethod(url_2)
    myPostMethod(url_1)
    myGetmethodFile()

    '''FALTA ESTUDIAR MODULO JSON'''