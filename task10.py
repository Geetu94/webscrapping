import json
from task5 import get_movie_details
l=get_movie_details()
def get_director_and_language():
    director_list=[]
    dic={}
    for i in l:
        if "director" in i:
            m=i["director"]
            for director in m:
                if director not in director_list:
                    director=director
                    director_list.append(director)
    dic={}
    for director in director_list:
        d={}
        for i in l:
            if director in i["director"]:
                if "language" in i:
                    for j in i["language"]:
                        if j in d:
                            d[j]=d[j]+1
                        if j not in d:
                            d[j]=1
        dic[director]=d
    file=open("task10.json","w")
    json.dump(dic,file,indent=4)
    file.close()
get_director_and_language()