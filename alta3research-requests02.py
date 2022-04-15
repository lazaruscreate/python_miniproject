#!/usr/bin/env python3
import requests

URL= "http://127.0.0.1:2224/info"

resp= requests.get(URL).json()
name = (resp['first_name'] + " " + resp['last_name'])
name_normal = name.replace(" ' ","")

position = resp['position']

team = resp['team']['full_name']

print(f"{name_normal} is a {position} for the {team}")
