import time

def calcProd():
    product = 1
    for i in range(1, 100000):
        product = product + 1
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))
