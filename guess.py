# this is a guess the number game
import random

print('Hello, what is your name?')
name = input()

print('Great, well ' + name + ' I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1,20)

for guessesTaken in range (1,6):
    print('Take a guess.')
    guess = int(input())

    if guess > secretNumber:
        print('Nope, too high')
    elif guess < secretNumber:
        print('Nope, too low')
    else:
        break # exit if guess == secretNumber

if guess == secretNumber:
    print('Nailed it! You got it in ' + str(guessesTaken) + ', ' + name + '.')
else:
    print('Unlucky, the number I am thinking of was ' + str(secretNumber) + '.')
