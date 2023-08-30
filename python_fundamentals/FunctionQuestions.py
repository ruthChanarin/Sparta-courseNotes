print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:

def divisor_list(n):
    list = []
    for x in range(1,n):
        if n % x == 0:
            list.append(x)
    return list



print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:

def factor_or_not(x,y):
    if x in divisor_list(y):
        return True
    elif y in divisor_list(x):
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

def alphabet_position_checker(letter):
    position = alphabet.index(letter)+1
    return(position)


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:

# Function which returns 

def ID_number_generator(name):
    ID_number_list = [alphabet_position_checker(letter) for letter in name]
    ID_number_string = ''.join(map(str,ID_number_list))
    ID_number = int(ID_number_string)
    return ID_number


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:

def password_generator(ID):
    ID_number = ID_number_generator(ID)
    ID_number_string = str(ID_number)
    ID_number_list = [digit for digit in ID_number_string]

    sum = 0
    for digit in ID_number_list:
        sum += int(digit)
    password = ID_number - sum
    return password



# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:

def prime_checker(num):
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

def prime_checker(num):
    try:
        if num > 1:
            for x in range(2,num):
                if num % x == 0:
                    return False
            else:
                return True
        elif num > 1: 
            return False
    except TypeError:
        print("Please enter valid numbers")
    



# -------------------------------------------------------------------------------------- #






