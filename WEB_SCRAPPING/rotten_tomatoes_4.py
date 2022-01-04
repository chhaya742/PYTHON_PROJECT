from bs4 import BeautifulSoup
import requests
import json
import pprint
url1='https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/'
page=requests.get(url1)
soup=BeautifulSoup(page.text,'html.parser')
table=soup.find('table',class_="table")
td=soup.find_all('td',class_='bold')
td1=soup.find_all('span',class_="tMeterScore")
name=table.find_all('a',class_="unstyled articleLink")
review=table.find_all('td',class_="right hidden-xs")
def tomato():
    list1=[]
    dict1={'position':'','name':'','rating':'','review':'','link':'','year':''}
    for j in range(0,len(td)):
        n=name[j].get_text()
        a=td[(j)].get_text().replace('.','')
        dict1['position']=int(a)
        dict1['name']=name[j].get_text().strip()
        dict1['rating']=td1[j].get_text().strip()
        dict1['review']=review[j].get_text()
        dict1['link']="https://www.rottentomatoes.com/"+name[j]['href']
        b=n.split()
        dict1['year']=b[-1][1:5]
        list1.append(dict1)
        dict1={'position':'','name':'','rating':'','review':'','link':'','year':''}
    with open("rotten.json","w") as f:
        json.dump(list1,f,indent=4)
# tomato()
# SECOND_TASK    
def group_by_year():
    with open("rotten.json","r") as f:
        data=json.load(f)
    year=[]
    for i in data:
        if i["year"] not in year:
            year.append(i["year"])
    dic1={}
    for j in year:
        n=[]
        for k in data:
            if j==k['year']:
                n.append(k)
        dic1.update({j:n})
    with open("movie_by_year_tomato.json","w") as f:
        json.dump(dic1,f,indent=6)
    # pprint.pprint(dic1)
# group_by_year()
## THIRD_TASK
data1=group_by_year()
def group_of_decade(data1):
    with open("movie_by_year_tomato.json","r") as f:
        data1=json.load(f)
    moviedec={}
    list1=[]
    for i in data1:
        mod=int(i)%10
        decade=int(i)-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10=i+9
        for x in data1:
            if int(x)<=dec10 and int(x)>=i:
                for v in data1[x]:
                    moviedec[i].append(v)
    with open("movie_Decade_tomato.json","w") as f:
        json.dump(moviedec,f,indent=6)
    # return moviedec
# group_of_decade(data1)
## FORTH TAKS
def scrape_movie_details():
    with open("rotten.json","r") as f:
        data2=json.load(f)
    # user=input("enter position ")
    m=1
    list1=[]
    for i in data2:
        if m==i['position']:
            a=str(i['link'])
            url=requests.get(a)
            soup=BeautifulSoup(url.text,'html.parser')
            main=soup.find_all("li",class_="meta-row clearfix")
            sub1=soup.find_all('div',class_="meta-label subtle")
            sub2=soup.find_all('div',class_="meta-value")
            dict1={}
            for j in range(0,len(main)):
                keys=sub1[j].get_text()
                value=sub2[j].get_text().strip().replace("\n",'')
                if keys=="Genre" or keys=="Original Language:" or keys=="Director:" or keys=="Producer:" or keys=="Writer" or  keys== "Production Co":
                    dict1.update({keys:list(value.split())})
                else:
                    dict1.update({keys:value})
            list1.append(dict1)
            pprint.pprint(list1)
            with open('dict_data.json',"w") as f:
                json.dump(list1,f,indent=5)
        m+=1
scrape_movie_details()










        




