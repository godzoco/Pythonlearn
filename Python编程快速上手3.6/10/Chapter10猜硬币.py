#!/usr/bin/env python3

# Chapter 10 Practice Debugging Coin Toss

import random

guess = ''
while guess not in (int(1), int(0)): #Changed heads and tails to 1 and 0 and made integers
    print('猜硬币，0或者1:') #Added 1 and 0
    guess = int(input()) #Turned string into integer

toss  = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('你赢了!')
else:
    print('错了，再猜!')
    guess = int(input()) #guess misspelled with three 's' instead of two and made guess integer
    if toss == guess:
        print('你赢了!')
    else:
        print('错了，表现糟糕.')
