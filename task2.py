from task1 import* 
def group_by_year():
    myfile=open("task1.json")
    opened_file=json.load(myfile)  
    movieName_dic={}
    for i in opened_file:
        year=i["year"]
        movie_list=[]
        for j in opened_file:
            y=j["year"]
            if year==y:
                movie_list.append(j)
                movieName_dic[year]=movie_list
    dict={}
    for i in sorted(movieName_dic):
        dict[i]=movieName_dic[i]  
    myfile=open("task2.json","w")
    json.dump(dict,myfile,indent=4)
    myfile.close() 
group_by_year()