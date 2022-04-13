#!/usr/bin/python3
import requests
import os
from apikeys import *


def main():
    #Clear the screen 
    os.system('cls' if os.name == 'nt' else 'clear')
    # Get the date input that we are looking for and concat it
    year = input("What year would you like? (ex. 2013): ")
    month = input("What month would you like? (ex. 07): ")
    day = input("What day would you like? (ex. 26): ")
    date = (year + "-" + month + "-" +  day)

    #Taking the information from the date and the api key from the git ignore file
    api_pre = (f"https://api.nasa.gov/planetary/apod?date={date}&api_key={api_key_priv}")
    api_resp = requests.get(api_pre)

    #taking the json file and parsing through it and taking what we need from it. 
    api_json = api_resp.json()
    date_json = (api_json['date'])
    description_json = (api_json['explanation'])
    url_json = (api_json['hdurl'])

    #Making the caption look better than normal json by taking away the single quotes
    desc_normal = description_json.replace(" ' ","")

    #Clear the screen again before you display the information
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Date: {date_json} \n\nDescription: {desc_normal} \n\nPhoto-URL: {url_json}")

if __name__ == "__main__":
    main()