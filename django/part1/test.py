
import random
guess = input("What is your guess? ")
print(type(guess))

print(type( int( list(guess)[0] == 1)))


digits = list(range(10))
random.shuffle(digits)
print(type(digits[:3][0]))

if 1 in [1,23]:
    print('ok 1')