import random

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

word_to_guess = getRandomWord(words)
# print(word_to_guess)
# word_display as string
word_display = ["_" for letter in word_to_guess]

# len(word_to_guess) * '_'
print("".join(word_display))
# user_guess = (input("Give me a letter: "))
lives_remaining = len(word_to_guess)
guesses = ''
while lives_remaining > 0 and "".join(word_display) != "".join(word_to_guess):
    print(f'Welcome to hangman! \nYou have {lives_remaining} attempts to guess the animal\n')
    letter = input("Give me a letter: ")
    for i in range(len(word_to_guess)):
        if word_to_guess[i] == letter:
            word_display[i] = word_to_guess[i]
    if letter not in word_to_guess:
        lives_remaining -= 1
        print(f'No match! You have {lives_remaining} lives remaining')
    if letter in guesses:
        print("you have already guesses this letter")
        lives_remaining -= 1
    if lives_remaining == 0:
        print(f"You lose the word was {word_to_guess}")
    if "".join(word_display) == "".join(word_to_guess):
        print('congrats you win!')
    guesses += letter
    print("Here are your guesses so far: " + guesses)
    print("".join(word_display))