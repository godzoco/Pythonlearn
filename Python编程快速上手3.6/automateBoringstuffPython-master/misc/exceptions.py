#exceptions

def spam(divided_by):
    try:
        return 42 / divided_by
    except:
        print('Invalid argument.')

print(spam(2))
print(spam(0))
print(spam(1))
