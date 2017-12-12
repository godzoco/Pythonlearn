#!/usr/bin/env python3

# Chapter 10 Coin Flip Debug

import random
heads = 0
for i in range(1, 1000):
    if random.randint(0,1) == 1:
        heads = heads + 1
    if i == 500:
        print('Halfway done...')
print('Heads came up ' + str(heads) + ' times.')
