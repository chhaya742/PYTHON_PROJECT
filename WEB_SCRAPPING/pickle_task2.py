
from bs4 import BeautifulSoup
import requests
import json
def scrape_top_list():
      urls1="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
      page=requests.get(urls1)
      soup=BeautifulSoup(page.text,'html.parser')
      div=soup.find('div',class_='_1gX7').span.get_text()
      var=int(div[1:5])
      var2=var//32
      var1=var2+1
      # print(var1)
      i=1
      list1=[]
      no=1
      dict1={'no':'','name':'','link':''}
      while i<=var1:
         urls= "https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="+str(i)
         page=requests.get(urls)
         soup=BeautifulSoup(page.text,'html.parser')
         pikle_name=soup.find_all('div',class_='UGUy')
         pikle_prize=soup.find_all('div',class_='_1kMS')
         pikle_link=soup.find_all('div',class_='_3WhJ')
         for j in range(0,len(pikle_name)):
               name=pikle_name[j].get_text()
               link="https://webscraper.io"+pikle_link[j].a['href']
               # dict1.update({'no':no,'name':name,'link':link})
               dict1['no']=no
               dict1['name']=name
               dict1['link']=link
               list1.append(dict1)
               no+=1
               dict1={'no':'','name':'','link':''}
         with open("pikle2.json",'w')as f:
            json.dump(list1,f,indent=6)
         i+=1
print(scrape_top_list())
         