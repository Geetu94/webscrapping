import json
from task5 import get_movie_details
all_data =get_movie_details()
def analyse_movies_directors():
    director_list=[]
    for i in all_data:
        if "director" in i:
            for j in i["director"]:
                director_list.append(j.strip())
        director_dic={}
        for i in director_list:
            if i in director_dic:
                director_dic[i]=director_dic[i]+1
            else:
                director_dic[i]=1
    file=open("task7.json","w")
    json.dump(director_dic,file,indent=4)
    file.close()
analyse_movies_directors()