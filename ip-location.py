#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import json

url_1 = 'https://www.iputilities.net/'
url_2 = 'https://ipapi.co/'
url_3 = 'https://ipinfo.io/'

def request_1(ip):
    payload = {'select': '/',
            'userip': ip,
            'whoisdb': 'APNIC'}

    print("---[www.iputilities.net]---")
    response = requests.post(url_1, data=payload)
    if 200 != response.status_code:
        print("status code: [",response.status_code,"]",response.text)
        return

    soup = BeautifulSoup(response.content, "html.parser")
    data = soup.find_all("td",id="answer")

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
    print("---[ipapi.co]---")
    response = requests.get(url_2 + ip + "/json")
    if 200 != response.status_code:
        print("status code: [",response.status_code,"]",response.text)
        return
    data = response.json()

    print("Country:",data["country_name"])
    print("City:",data["city"])
    print("Latitude,Longtude:",str(data["latitude"]) + "," + str(data["longitude"]))
    print("Org:",data["org"])

def request_3(ip):
    headers={'referer':'https://ipinfo.io/'}

    print("---[ipinfo.io]---")
    response = requests.get(url_3 + "widget/demo/" + ip, headers=headers)
    if 200 != response.status_code:
        print("status code: [",response.status_code,"]",response.text)
        return

    data = response.json()

    print("Country:",data["country"])
    print("City",data["city"])
    print("Latitude,Longtude:",data["loc"])

def main():
    ip_address = input("IP Address> ")

    print()
    request_1(ip_address)
    print()
    request_2(ip_address)
    print()
    request_3(ip_address)
    print()

if __name__ == '__main__':
    main()
