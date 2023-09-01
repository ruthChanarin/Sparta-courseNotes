
print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:
print(x[0:5])



print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:

# loop through list; if number is even, return number

for number in x:
    if number % 2 == 0: 
        print(number)



print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:

# run while loop for variable counter until y > 5 to run through list checking for evenness

counter = 0 
while(counter<5):
    if x[counter] % 2 ==0:
        print(x[counter])
    counter += 1




# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:

# List comprehension storing the 0 index (the initial) for each name in list of names

initials = [name[0] for name in names]
print(initials)



print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:

# List comprehension storing the index of the space in each name

space_index = [name.index(" ") for name in names]
print(space_index)



print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:

# List comprehension storing the intial, then first letter of surname (located in the index after the space)

first_and_last_initial = [name[0] + name[name.index(" ")+1] for name in names]
print(first_and_last_initial)

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a:

# Run a for loop through the lists, printing each one where the length of the list equals the length of 
# a set of that list (without duplicates), to check for duplicates. 
# If no duplicates are in list (list = set), we print the list

for list in list_of_lists:
    if len(list) == len(set(list)):
        print(list)


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:


while True:
    try: 
        n = int(input("Give me a number higher than 100: "))
        if n < 100: 
            raise ValueError("Try again")
        break
    except ValueError:
        print("Try again")

print(f"The number you entered is: {n}")

print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:

# Create function to check primeness of a number

def prime_number_checker(number: int) -> bool:
    for x in range(2,number):
        if number % x == 0: 
            print("This number is not a prime.")
            return False
        else:
            print("This number is prime.")
            return True


# re-run program, then run prime_number_checker function on number 

while True:
    try: 
        n = int(input("Give me a number higher than 100: "))
        if n < 100: 
            raise ValueError("Try again")
        break
    except ValueError:
        print("Try again")


print(f"The number you entered is: {n}")
prime_number_checker(n)
