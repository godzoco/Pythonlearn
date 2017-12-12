# Validate input

while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Pleas enter a number for your age.')

