import requests
from bs4 import BeautifulSoup
import pprint

def  scrape_movie_cast(movie_caste_url):
    response=requests.get(movie_caste_url)
    soup=BeautifulSoup(response.text,"html.parser")
    # for  i in range(0,len(movie_caste_url)):
    # return soup
    main_div=soup.find("table", class_="cast_list")
    name=main_div.find_all("td",class_="")
    cast_name=[]
    cast_ids_name=[]
    movie_cast_list=[]
    for i in name:
        dic={}
        data=i.get_text().strip()
        cast_name.append(data)
        id_name=i.a["href"]
        cast_id=""
        for j in range(6,len(id_name)):
            if "/" not in id_name[j]:
                cast_id+=id_name[j]
            else:
                break
        # return(cast_id)
        cast_ids_name.append(cast_id)
    # return(cast_ids_name)
    
    # return(cast_name)
        for k in range(0,len(cast_name)):
            dic={}
            dic["imdb_id_no."]=cast_ids_name[k]
            dic["name"]=cast_name[k]
        movie_cast_list.append(dic)

    return(movie_cast_list)

url='https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast'
# pprint.pprint(scrape_movie_cast(url))