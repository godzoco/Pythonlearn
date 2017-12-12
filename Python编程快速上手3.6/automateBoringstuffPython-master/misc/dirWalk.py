#! /user/bin/env python3

# Chapter 9 Walk Directory with os.walk()

import os

for folderName, subfolders, filenames in os.walk(os.getcwd()):
    print('The current folder is: ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

        for filename in filenames:
            print('FILE INSIDE ' + folderName + ': ' + filename)

        print('')
    
