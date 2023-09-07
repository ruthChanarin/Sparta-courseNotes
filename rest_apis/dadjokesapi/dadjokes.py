
import requests
import json
import csv
from api import random_joke_generator 


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

  

