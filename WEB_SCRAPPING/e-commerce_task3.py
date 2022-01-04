from bs4 import BeautifulSoup
import requests
import json
url1="https://webscraper.io/test-sites"
page=requests.get(url1)
soup=BeautifulSoup(page.text,'html.parser')
div=soup.find('div',class_='container test-sites')
div1=div.find_all("div",class_="col-md-7 pull-right")
def e_commerce():
    list1=[]
    dict1={'s_no':'','name':'','link':'',}
    s_no=1
    for i in range(0,len(div1)):
        name=div1[i].a.get_text().strip()
        link='https://webscraper.io'+div1[i].a['href']
        dict1['s_no']=s_no
        dict1['name']=name
        dict1['link']=link
        s_no+=1
        list1.append(dict1)
        dict1={'s_no':'','name':'','link':'',}
    with open("e_commerce.json","w") as f:
        json.dump(list1,f,indent=5)
print(e_commerce())	
