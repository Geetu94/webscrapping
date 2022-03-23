import json
from task5 import get_movie_details
all_data =get_movie_details()
def analyse_movies_language():
    language_list=[]
    for i in all_data:
        if "language" in i:
            for j in i["language"]:
                language_list.append(j)
            language_dic={}
            for i in language_list:
                if i in language_dic:
                    language_dic[i]=language_dic[i]+1
                else:
                    language_dic[i]=1
    file=open("task6.json","w")
    json.dump(language_dic,file,indent=4)
    file.close()
analyse_movies_language()