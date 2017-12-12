

import os
import shutil

def selectiveCopy(folder):
    folder = os.path.abspath(folder)
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if not filename.endswith('.pdf'):
                continue
            print(filename)
            shutil.copy(filename, 'e:\\2') 
            #Commented out to protect against accidental copying
            print('Copying ' + filename + '...') #Print only to verify working correctly

#selectiveCopy(r'C:\Users\username\pdffolder')
#这里的　r的使用在字符串　后面　就是不转义
selectiveCopy('e:\\n')
print('Done')
