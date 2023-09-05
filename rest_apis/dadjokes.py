
import requests
from pprint import pprint
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


# function to export the joke to a json file

def joke_to_json(joke):
    with open("joke_collection.json", "w") as jsonfile:
        json.dump(joke, jsonfile)


# function to export the joke to a csv file

def joke_to_csv(joke):
    with open("joke_csv_file.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(joke.split())


# function to take in user input about which type of file they'd like to export their joke(s) to

def json_or_csv():
    while True:
        choice = input("Would you like to export your jokes to a JSON or a CSV file? ").upper()
        if choice in ('JSON', 'CSV'):
                return choice
        
        # else clause in case of invalid input

        else:
            print("Please enter a valid option.")


# function to determine how many jokes to create using user input

def how_many_jokes():
    while True:
        how_many = input("How many jokes do you want? ")
        try: 
            number_of_jokes = int(how_many)
            break

# except clause to deal with faulty, non-numerical input

        except ValueError:
            print("Please enter a valid number")    
    return number_of_jokes


# function to run joke outputter, using above functions to ask the user how many jokes they'd
# like, then outputting them to a file type of their choosing

def joke_outputter():
    number = how_many_jokes()
    jokes = ''
    for x in range(number):
        joke = random_joke_generator()
        jokes += joke 
    
    if json_or_csv() == 'JSON':
        joke_to_json(jokes)   

    elif json_or_csv() == 'CSV':
        joke_to_csv(jokes)
  

joke_outputter()

# function to enable to user to return jokes based on a keyword search, which are then printed to a json file

def joke_by_keyword():

    keyword = input("I want a joke about... ")
    url = f"https://icanhazdadjoke.com/search?term={keyword}"
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    data = requests.get(url, headers=headers)

    result = data.json().get('results')

    print(result)
    print(type(result))


    for item in result: 
        print(item['joke'])

joke_by_keyword()


