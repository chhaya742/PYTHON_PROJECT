from bs4 import BeautifulSoup
import requests
import pprint
import json
url1="https://www.imdb.com/india/top-rated-indian-movies/"
page=requests.get(url1)
# print(var)
# pprint.pprint(page.text)
soup=BeautifulSoup(page.text,'html.parser')
def scrape_top_list():
    main_div=soup.find('div',class_='lister')
    # return main_div
    tbody=main_div.find('tbody',class_='lister-list')
    # return tbody
    trs=tbody.find_all('tr')
    # return trs
    movie_rank=[]
    movie_name=[]
    year_of_realease=[]
    movie_urls=[]
    movie_rating=[]
# print(scrape_top_list())
    for tr in trs:
        position=tr.find('td',class_="titleColumn").get_text().strip()
        # return (position)
# print(scrape_top_list())
        rank= ''
        for i in position:
            if '.' not in i :
                rank=rank+i
            else:
                break
        movie_rank.append(rank) 
        
#     return movie_rank
# print(scrape_top_list())


        title=tr.find('td',class_="titleColumn").a.get_text()
        movie_name.append(title)
        with open("name.json","w") as f:
            json.dump(movie_name,f,indent=6)
        # return title
#     return movie_name
# print(scrape_top_list())
   

        year=tr.find('td',class_="titleColumn").span.get_text()
        year_of_realease.append(year)
        with open("year.json","w") as f:
            json.dump(year_of_realease,f,indent=6)
#         # return year
#     return year_of_realease
# print(scrape_top_list())
    
        rating=tr.find('td',class_='ratingColumn imdbRating').strong.get_text()
        movie_rating.append(rating)
        with open("rating.json","w") as f:
            json.dump(movie_rating,f,indent=6)
#         # return rating
# #     return movie_rating
# # print(scrape_top_list())
    

        link=tr.find('td',class_='titleColumn').a['href']
        movie_link="https:www.imdb.com"+link
        movie_urls.append(movie_link)
        with open("link.json","w") as f:
            json.dump(movie_urls,f,indent=6)

        # return link
#     print( movie_urls)
# scrape_top_list()


    
    
    details={'position':'','name':'','year':'','rating':'','urls':''}
    top_movies=[]
    i=0
    for i in range(0,len(movie_rank)):
        details["position"]=int(movie_rank[i])
        details["name"]=str(movie_name[i])
        year_of_realease[i]=year_of_realease[i][1:5]
        details["year"]=int(year_of_realease[i])
        details["rating"]=float(movie_rating[i])
        details["urls"]=movie_urls[i]
        top_movies.append(details)
        details={'position':'','name':'','year':'','rating':'','urls':''}
    with open("movie_list.json","w") as f:
        json.dump(top_movies,f,indent=6)
    return (top_movies) 
# pprint.pprint(scrape_top_list())
scrapped=scrape_top_list()
def group_by_year(movies):
    year=[]
    for i in movies:
        if i['year'] not in year:
            year.append(i['year'])
#     return year
# print(group_by_year(scrapped))
    dic1={}
    for j in year:
        n=[]
        for k in movies:
            if j==k['year']:
                n.append(k)
        dic1.update({j:n})
    # dic1.sort()
    with open("movie_by_year.json","w") as f:
        json.dump(dic1,f,indent=6)
    return dic1
        # pprint.pprint(dic1)
dec_arg=group_by_year(scrapped)
def group_of_decade(movies):
    moviedec={}
    list1=[]
    for i in movies:
        mod=i%10
        decade=i-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10=i+9
        for x in movies:
            if x<=dec10 and x>=i:
                for v in movies[x]:
                    moviedec[i].append(v)
    with open("movie_Decade.json","w") as f:
        json.dump(moviedec,f,indent=6)
    # return moviedec
pprint.pprint(group_of_decade(dec_arg))





        





