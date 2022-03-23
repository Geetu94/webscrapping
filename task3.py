from math import remainder
from task1 import*
myfile=open("task1.json")
opened_file=json.load(myfile)
main_dic={}
decade_list=[]
for i in opened_file:
    rem=i["year"]%10
    decade=i["year"]-rem
    if decade not in decade_list:
        decade_list.append(decade)
# list=[]
for i in decade_list:
    list1=[]
    for j in  range(i,i+9):
        for k in opened_file:
            if j==k["year"]:
                list1.append(k)
    main_dic[i]=list1
file=open("task3.json","w")
json.dump(main_dic,file,indent=4)
file.close() 
    