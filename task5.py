# import json
# from bs4 import BeautifulSoup
# from task1 import scrap_top_list
# from Tasks4 import movie_details
# movie=scrap_top_list()
# def get_movie_list_details():
#     list=[]
#     for i in movie:
#         a=movie_details(i["movieName"],i["Url"])
#         list.append(a)
#         print(list)
#     with open ("task_5.json","w+") as file:
#         json.dump(list,file,indent=4)
# get_movie_list_details()



import json
from pprint import pprint
f=open("Task4.json","r")
movie_list=json.load(f)
g_movie,top_movie=0,[]
def scrape_movie_details():
    g_movie=0
    for i in movie_list:
        top_movie.append(movie_list[i])
        if g_movie==10:
            break
        g_movie+=1
    file=open("task5s.json","w")
    json.dump(top_movie,file,indent=4)
    file.close()
    return top_movie
print(scrape_movie_details())
