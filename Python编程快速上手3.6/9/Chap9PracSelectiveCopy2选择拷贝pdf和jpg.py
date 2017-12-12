

import os
import shutil

#os.chdir('e:\\')
def selectiveCopy(folder):
    folder = os.path.abspath(folder)
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if not filename.endswith('.pdf'):
                continue
            print(filename)
            #感谢刘工　刘嗣林
            a=os.path.join(foldername, filename)
            shutil.copy(a,'e:\\') 
            #如果shutil.copy(a,'e:\\２')
            #没有２这个文件夹，就ＰＤＦ复制到Ｅ盘然后改名字叫２
            
            #Commented out to protect against accidental copying
            print('Copying ' + filename + '...') #Print only to verify working correctly

#selectiveCopy(r'C:\Users\username\pdffolder')
#这里的　r的使用在字符串　后面　就是不转义
selectiveCopy('e:\\n')
print('Done')
