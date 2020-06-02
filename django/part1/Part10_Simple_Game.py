###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
# digits = list(range(10))
# random.shuffle(digits)
# print(digits[:3])
# x= digits[:3];
# print( type(x))

# Another hint:
# guess = input("What is your guess? ")
# print(guess)
# print(list(guess)[0])

def _check(target,temp):
    result = 'Nope'
    for i in range(len(target)):
        t =int(temp[i])
        if t == target[i]:
            result = True
            break
        elif t in target:
            result ='Close'
            break


    return result

def guessDigits():
    welcome = 'Welcome the guess digits Game! Good luck!'
    digits = list(range(10))
    random.shuffle(digits)
    target = digits[:3]
    print(welcome)
    print('Computer have generator the num, you can begin to guess')
    print(target)
    result = False
    guess = 1
    while bool(1-result):
        guess = input('What is your guess?')
        checkResult = _check(target,guess)
        if type(checkResult) == type('hello'):
            print(checkResult)
        else:
            result =checkResult

    print('Bingo! you guess It,Target is{},and your guess is{}'.format(target,guess))

guessDigits()

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
