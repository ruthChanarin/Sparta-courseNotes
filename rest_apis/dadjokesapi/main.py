

from api import random_joke_generator, joke_by_keyword
from dadjokes import joke_to_json, joke_to_csv, json_or_csv, how_many_jokes


# function to run joke outputter, asking the user how many jokes they'd
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



# function to enable to user to return jokes based on a keyword search, which are then printed to a json file

def get_jokes_by_keyword():

    result = joke_to_json(joke_by_keyword())

    for item in result: 
        print(item['joke'])

