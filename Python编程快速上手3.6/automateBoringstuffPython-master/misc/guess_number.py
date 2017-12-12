# Guess the number game

import random
secret_number = random.randint(1, 10)
print('I am thinking of a number between 1 and 10.')

# Ask Player to guess 6 times
for guess_taken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secret_number:
        print('Your guess is too low')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break

if guess == secret_number:
    print('Good job! You guessed my number in ' + str(guess_taken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secret_number))
    
