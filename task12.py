import json
import requests
from bs4 import BeautifulSoup
def scrape_movie_cast(url):
    page=requests.get(url) 
    soup=BeautifulSoup(page.text,"html.parser")
    div=soup.find('div',class_="castSection")
    di=div.find_all("div",class_="cast-item media inlineBlock")
    di2=div.find_all("div",class_="cast-item media inlineBlock moreCasts hide")
    list=[]
    for i in di:
        dic1={}
        a=i.find("a")["href"][11:]
        dic1["cast_name"]=a
        list.append(dic1)
    for i in di2:
        dic2={}
        b=i.find("a")["href"][11:]
        dic2["cast_name"]=b
        list.append(dic2)
    file=open("task12.json","w")
    json.dump(list,file,indent=4)
    file.close()
    return list
scrape_movie_cast("https://www.rottentomatoes.com//m/toy_story_4")

