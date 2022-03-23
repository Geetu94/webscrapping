from task1 import scarap_top_movies
from task4 import one_movie
import json
t1=scarap_top_movies()
movies_data=t1
def get_movie_details():
    movies_list=[]
    for i in movies_data:
        link=i['url']
        movies_list.append(one_movie(link))
    file=open("task5.json","w")
    json.dump(movies_list,file,indent=4)
    file.close()
    return movies_list
get_movie_details()




