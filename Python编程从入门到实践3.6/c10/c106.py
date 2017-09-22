def tj():    
    try:
        x = input("Give me a number: ")
        x = int(x)
    
        y = input("Give me another number: ")
        y = int(y)
    
    except ValueError:
        print("Sorry, I really needed a number.")
        tj()
    else:
        sum = x + y
        print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")
        
tj()