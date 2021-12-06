import json
import requests
f=open("task1s.json","r")
c=json.load(f)
print(c)
def group_by_year(movies):
    years=[]
    for i in movies:
        yr=i["year"]
        if yr not in years:
            years.append(yr)
    movie_dict = {i:[]for i in years}
    for j in movies:
        yy = j["year"]
        for x in movie_dict:
            if str(yy) == str(x):
                movie_dict[x].append(j)
    h = json.dumps(movie_dict,indent = 4)
    with open("task2s.json","w") as file:
        file.write(h)
group_by_year(c)

