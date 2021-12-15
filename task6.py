import json 
m_f = open("Task4.json","r")
movie_list = json.load(m_f)
langs_list,set1,dict_ana_lang = [],set(),{}

def Analysis_movie_language():
    for movie_det in movie_list:
        if "Language" in movie_det:
            langs_list.append("Language")
            set1.add("Language")
    for langs in set1:
        dict_ana_lang[langs]=langs_list.count(langs)
    file = open("task6s.json","w")
    json.dump(dict_ana_lang,file,indent = 4)
    file.close()
Analysis_movie_language()
