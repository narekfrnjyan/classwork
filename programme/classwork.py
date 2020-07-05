import requests
import re

req = requests.get("https://httpstatuses.com/")
document = req.content.decode("utf-8")

f = open("index.html", "w")
f.write(document)
f.close()
#1st
with open("index.html","r") as file:
    f1=file.readlines()

    d=len(f1)
    q=0
    d1=[]
    while q<d:
        f1[q]=f1[q].strip(" ")
        if f1[q][0:6]!="<li><a":
            f1.remove(f1[q])
            d-=1
        else:
            q+=1
    list1=[]
    for i in range(len(f1)):
        f1[i]=f1[i].lstrip("<")
        f1[i] = f1[i].rstrip(">\n")
        count=f1[i].count(">")
        s=""
        for j in range(count):
            s+=f1[i][f1[i].index(">")+1:f1[i].index("<")]
            f1[i]=f1[i][f1[i].index("<")+1:]
        list1.append(s)
    for i in list1:
        print(i[0:4]+"-"+i[5:])
#second
with open("index.html","r") as file:
    n=file.readlines()
    for i in n:
        x=re.findall("^<li><a",i.strip(" "))
        if x:
            q=i.strip(" ").lstrip("<").rstrip(">\n")

            s=q.count(">")
            d=""
            for j in range(s):
                d += q[q.find(">") + 1:q.find("<")]
                q=q[q.find("<")+1:]
            print(d)

#third
with open("index.html", "r") as file2:
    for i in file2:
        row = file2.readline()
        reg=re.findall("^<li><a",row.strip(" "))
        if reg:
            list=row.split(">")
            for k in range(len(list)):
                if list[k][0:3].isdigit():
                    print(list[k][0:3]+"-"+list[k+1][:list[k+1].index("<")])
