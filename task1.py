import json
import requests
from bs4 import BeautifulSoup
url="https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/"
page=requests.get(url) 
soup=BeautifulSoup(page.text,"html.parser")
# print(soup.prettify)
def scarap_top_movies():
    list=[]
    main_div=soup.find('div',class_='container')
    tbody=main_div.find('div',class_="panel-body content_body allow-overflow")
    table=tbody.find('table', class_="table")
    table1=table.find_all('tr')
    for i in table1:
        dic={}
        td=i.find_all("td")
        for k in td:    
            movie_name=i.find('a',class_='unstyled articleLink')["href"][3:]
            dic["name"]=movie_name
            total_reviews=i.find('td',class_='right hidden-xs').get_text()
            dic["review"]=int(total_reviews)
            total_rating=i.find('span',class_='tMeterScore').get_text()[1:3]
            dic["rating"]=float(total_rating)
            all_year=i.find('a',class_='unstyled articleLink').get_text() 
            year=all_year.strip()
            dic["year"]=int(year[-5:-1])
            url=i.find("a",class_='unstyled articleLink')["href"]
            one="https://www.rottentomatoes.com/"+url
            dic["url"]=one
        list.append(dic)
        if {} in list:
            list.remove({})
        myfile=open("task1.json","w")
        json.dump(list,myfile,indent=4)
        myfile.close()
    return list
scarap_top_movies()