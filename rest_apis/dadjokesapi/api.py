
import requests
import json
import csv


# function to generate a random joke from the Dad Joke API

def random_joke_generator(): 
    try: 
        url = "https://icanhazdadjoke.com/"
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        data = requests.get(url, headers=headers)
        joke = data.json().get('joke')

# except clause which returns a basic joke should there be any problem

    except: 
        joke = "I considered moving to Moscow, but there's no point Russian into things"
    
    return joke


# function to enable to user to return jokes based on a keyword search, which are then printed to a json file

def jokes_by_keyword():

    keyword = input("I want a joke about... ")
    url = f"https://icanhazdadjoke.com/search?term={keyword}"
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    data = requests.get(url, headers=headers)

    result = data.json().get('results')

    return result