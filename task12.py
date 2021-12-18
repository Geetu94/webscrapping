import json
import requests
import pprint
from bs4 import BeautifulSoup
movie_file = open("task1s.json","r")
movie_data = json.load(movie_file)
movie_link_list = []
def scrap_movie_cast():
    for movie_det in movie_data:
        movie_link_list.append(movie_det["movie_link"])
    for m_link in movie_link_list:
        url = requests.get(m_link+"fullcredits?ref_=tt_cl_sm#cast")
        soup = BeautifulSoup(url.text,"html.parser")
        c_movie = soup.find("table",class_="cast_list")
        actor_cast = c_movie.find_all("td",class_="")
        list_cast = []
        for ids in actor_cast:
            dic ={}
            dic["imdb_id"] = ids.a["href"][7:15]
            dic["name"] = ids.text.strip()
            list_cast.append(dic)
        file = open(m_link[28:37]+"_cast.json","w")
        json.dump(list_cast,file,indent = 4)
        file.close()
        print(list_cast)
scrap_movie_cast()
