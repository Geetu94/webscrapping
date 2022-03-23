import json
from task5 import get_movie_details
all_data =get_movie_details()
def analyse_movies_genre():
    genre_list=[]
    for i in all_data:
        if "genre" in i:
            for j in i["genre"]:
                genre_list.append(j)
            genre_dic={}
            for i in genre_list:
                if i in genre_dic:
                    genre_dic[i]=genre_dic[i]+1
                else:
                    genre_dic[i]=1
    file=open("task11.json","w")
    json.dump(genre_dic,file,indent=4)
    file.close()
analyse_movies_genre()