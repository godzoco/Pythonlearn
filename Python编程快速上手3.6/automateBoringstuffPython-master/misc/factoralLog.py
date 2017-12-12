#!python3

# Chapter 10 Factoral Log

import logging
logging.basicConfig(filename='errorLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of Program')

def factorial(n):
    logging.debug('Start of Factorial(%s%%)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of Factorial(%s%%)' % (n))
    return total

print(factorial(5))
logging.debug('End of Program')
