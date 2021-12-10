import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup
f=open("task1s.json","r")
x=json.load(f)
list0=[]
def scrape_movie_details():
    for i in x:
        for j in i:
            if j =="movie_link":
                list0.append(i[j])
    list1=[]
    c=1
    dict1={}
    for j in list0:
        url=requests.get(j)
        soup=BeautifulSoup(url.text,"html.parser")
        ul=soup.find_all("ul",class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base")
        tit=soup.find("div",class_="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt")
        title=soup.find("h1",class_="TitleHeader__TitleText-sc-1wu6n3d-0")
        a=tit.find_all("li",class_="ipc-inline-list__item")
        s=0
        for k in a:
            if s==2:
                dict1["runtime"]=k.text

            s+=1
        # a=tit.find("li",class_="ipc-inline-list__item")
        for j in ul:
            list2=[]
            if "Language" in j.text:
                li = j.find_all("li")
                for i in li:
                    if "Language" in i.text:
                        div = i.find("div")
                        a= div.find_all("a")
                        for lan in a:
                            list2.append(lan.get_text())
                        dict1["language"]=list2
                    if "Country" in i.text:
                        a=i.find("a")
                        dict1["Country"]=a.get_text()
                    if "Release" in i.text:
                        a=i.find("li")
                        dict1["year"]=a.text
        dict1["movie_name"]=soup.find('h1').text
        dict1["genre"]=soup.find("span",class_="ipc-chip__text").text
        dict1["director"]=soup.find("div",class_="ipc-metadata-list-item__content-container").text
        dict1["img_url"]='https://www.imdb.com/'+(soup.find("a",class_="ipc-lockup-overlay ipc-focusable")["href"][:-14])
        dict1["bio_title"]=soup.find("span",class_="GenresAndPlot__TextContainerBreakpointL-cum89p-3 bgIqtV")
        pprint(dict1)
        list1.append(dict1.copy())
    return list1
print(scrape_movie_details())
