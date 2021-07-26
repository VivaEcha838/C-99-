import time
import os
import shutil

def removingFiles():
    path = input("Enter the source folder name : ")
    days = 30
    seconds = time.time()-(days*24*60*60)

    if os.path.exists(path):
        print("huigefiefug")
        for root, dirs, files in os.walk(path):
            print("viva")
            if seconds > os.stat(path).st_ctime:
                shutil.rmtree(path)
removingFiles()

        
   

    

 

    