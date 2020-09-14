import requests
from bs4 import BeautifulSoup
import pprint 

def scrape_movie_details(movie_detail_url):
    # return(soup)
    # movie_detail_url='https://www.imdb.com/title/tt0066763/'
    response=requests.get(movie_detail_url)
    response_txt=response.text
    soup=BeautifulSoup(response_txt,"html.parser")

    name_div=soup.find("div",class_="title_wrapper").h1.get_text().strip()
    name=""
    for i in name_div:
        if i != "(":
            name=name+i
        else:
            break
    movieName=name.strip()
    # return(movieName) 
    main_div=soup.find("div",class_="plot_summary_wrapper")
    next_div=main_div.find("div",class_="plot_summary")
    director_div=next_div.find("div",class_="credit_summary_item").h4.get_text().strip()
    director=""
    for i in director_div:
        if i !=":":
            director+=i
        else:
            break
    # return(director)
    director_name=soup.find("div",class_="credit_summary_item")
    all_names=director_name.find_all("a")
    direct_name=[]
    for name in all_names:
        direct_name.append(name.get_text().strip())
    # return(direct_name)
        
    # url=soup.find("div",class_="slate_wrapper")
    url_div=soup.find("div",class_="poster").img["src"]
    movie_bio=next_div.find("div",class_="summary_text").get_text().strip()
    # return(movie_bio.strip())
    main_genres=soup.find("div",class_="subtext")
    movie_genre=main_genres.find_all("a")
    genre_div=movie_genre.pop()
    time=main_genres.time.get_text().strip()
    for i in range(0,len(time)):
        movie_time=int(time[0])*60+int(time[3])
        # return(movie_time)
    genr_lis=[]
    for k in movie_genre:
        genr_lis.append(k.get_text())
    # return(genr_lis)
    article=soup.find("div",id="titleDetails",class_="article")
    text_blkk=article.find_all("div")
    # movie_detalis_dict={}
    language=[]
    for i in text_blkk:
            try:
                if "Country:" == i.find("h4").get_text():
                    Country = i.find("a").get_text()
                    # country.append(Country)
                    # return Country
                elif "Language:" == i.find("h4").get_text():
                    Language = i.find("a").get_text()
                    language.append(Language)
            except:
                pass
    # return(value_lis)
    movie_detalis_dict={}
    movie_detalis_dict["name"]=movieName
    movie_detalis_dict["Director"]=direct_name
    movie_detalis_dict["poster_img_url"]=url_div
    movie_detalis_dict["country"]=Country
    movie_detalis_dict["language"]=language
    movie_detalis_dict["bio"]=movie_bio
    movie_detalis_dict["runtime"]=movie_time
    movie_detalis_dict["genre"]=genr_lis


    return(movie_detalis_dict)
movie_list_detail=(scrape_movie_details('https://www.imdb.com/title/tt0066763/'))
# pprint.pprint (movie_list_detail)


