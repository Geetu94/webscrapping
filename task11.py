import json
file = open("Task4.json","r")
m_dict = json.load(file)
genre_dict = {}
def analyse_genre():
    for i in m_dict:
        if "Genre" in i:
            genre_dict[i]=m_dict[i]
    file = open("task11s.json","w")
    json.dump(genre_dict,file,indent = 4)
    file.close()
analyse_genre()
