# The Collatz Sequence

def collatz(number):
    global result
    if number % 2 == 0:
        print(str(number // 2))
        result = number // 2
        return result
    elif number % 2 == 1:
        print(str(3 * number + 1))
        result = 3 * number + 1
        return result

print('Enter number:')
while True:
    try:
        number = int(input())
    except ValueError:
        print('The value must be an integer!')
        continue
    collatz(number)
    if result == 1:
        break
