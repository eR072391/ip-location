#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import json

url_1 = 'https://www.iputilities.net/'
url_2 = 'https://ipapi.co/'

def request_1(ip):
    payload = {'select': '/',
            'userip': ip,
            'whoisdb': 'APNIC'}

    response = requests.post(url_1, data=payload)
    soup = BeautifulSoup(response.content, "html.parser")
    data = soup.find_all("td",id="answer")

    print("---[www.iputilities.net]---")
    hostname = str(data[1])
    print("HOST NAME:", hostname[16:-5])
    country = str(data[2])
    print("Country:",country[16:-36])
    city = str(data[6])
    print("City:",city[26:-5])
    La = str(data[7])
    Lo = str(data[8])
    print("Latitude,Longitude:", La[26:-5] + "," + Lo[26:-5])

def request_2(ip):
    response = requests.get(url_2 + ip + "/json")
    data = response.json()

    print("---[ipapi.co]---")
    print("Country:",data["country_name"])
    print("City:",data["city"])
    print("Latitude,Longtude:",str(data["latitude"]) + "," + str(data["longitude"]))
    print("Org:",data["org"])

def main():
    ip_address = input("IP Address> ")

    print()
    request_1(ip_address)
    print()
    request_2(ip_address)

if __name__ == '__main__':
    main()
