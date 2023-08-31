print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:

# create function which takes in an integer, runs through the number from 1 to the integer, and returns 
# any divisors, adding them to a list

def divisor_list(number: int) -> list:
    divisors = []
    for x in range(1,number):
        if number % x == 0:
            divisors.append(x)
    return divisors



print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:

# Create a function which takes in two integers, and checks if each is a divisor of the other, by running 
# my divisor list function from before & checking if it contains the number

def factor_or_not(num1: int, num2: int) -> bool:
    if num1 in divisor_list(num2):
        return True
    elif num2 in divisor_list(num1):
        return True
    else:
        return False
    


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Create function which takes in a letter and checks the index of it in the alphabet list (adding 1 to start 
# at 1 rather than 0)

def alphabet_position_checker(letter: str) -> int:
    position = alphabet.index(letter)+1
    return(position)


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:

# Function which returns ID number consisting of positions of each letter in alphabet, using function from before

def id_number_generator(name: str) -> str:
    id_number_list = [alphabet_position_checker(letter) for letter in name]
    id_number = ''.join(map(str,id_number_list))
    return id_number


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:

# Create function which inputs a name, and turns it into a secret passord

def password_generator(name: str) -> int:
    id_number = id_number_generator(name)
    id_number_list = [digit for digit in id_number]

# adds each digit onto a sum to find total, then subtracts that from the id number
    sum = 0
    for digit in id_number_list:
        sum += int(digit)
    password = id_number - sum
    return password



# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:

# Function which checks if a number has any divisors; if not it's a prime

def prime_checker(num: int) -> bool:
    if num > 1:
        for x in range(2,num):
            if num % x == 0:
                return False
        else:
            return True
    else: 
        return False




print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:

# add a try and except clause onto the previous function, to deal with input errors

def prime_checker(num: int) -> bool:
    try:
        if num > 1:
            for x in range(2,num):
                if num % x == 0:
                    return False
            else:
                return True
        else:
            return False
    except TypeError:
        print("Please enter valid numbers")
    



# -------------------------------------------------------------------------------------- #






