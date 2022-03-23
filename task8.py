import requests
import os
import json
from task1 import*
file=open("task1.json","r+")
a=json.load(file)
file.close()
def text():
    for i in a:
        path="/home/dell44/Desktop/task8"+i["name"]+".text"
        if os.path.exists(path):
            pass
        else:
            myfile=open(path,"w")
            url=requests.get(i["url"])
            myfile.write(url.text)
            myfile.close()
            
text()