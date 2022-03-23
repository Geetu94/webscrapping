from task12 import scrape_movie_cast
from task4 import one_movie
import json
all_data_list=[]
def scrape_all_movie_cast(url):
    t12=scrape_movie_cast(url)
    t4=one_movie(url)
    dic={}
    t4["cast"]=t12
    all_data_list.append(t4)
    file=open("task13.json","w")
    json.dump(all_data_list,file,indent=4)
    file.close()
scrape_all_movie_cast("https://www.rottentomatoes.com//m/inside_out_2015")