
from imdb_1_task import *
# from imdb_4_task import *

def get_movie_list_details():
    # return(details)
    lis=[]
    for i in range(0,10):
        url=movie_details[i]['movie url']
        lis.append(url)
    # return(lis)
    ovreall_10_movie_detail=[]
    name_lis=[]
    director_nam_list=[]
    poster_img=[]
    movie_bio_lis=[]
    runtime=[]
    gener_movie=[]
    country=[]
    language=[]
    for index in lis:
        response=requests.get(index)
        soup=BeautifulSoup(response.text,"html.parser")
        name=soup.find("div",class_="title_wrapper").h1.get_text().strip()
        naam=""
        for j in name:
            if j !="(":
                naam+=j
            else:
                break
        # return(naam.strip())
        name_lis.append(naam.strip())
    # return(name_lis)
        main_div=soup.find("div",class_="plot_summary_wrapper")
        next_div=main_div.find("div",class_="plot_summary")
        director_div=next_div.find("div",class_="credit_summary_item")
        all_names=director_div.find_all("a")
        direct_name=[]
        for name in all_names:
            direct_name.append(name.get_text().strip())
        director_nam_list.append(direct_name)
    # return(director_nam_list)
        poster_url=soup.find("div",class_="poster").img["src"]
        poster_img.append(poster_url)
    # return(poster_img)
        bio=next_div.find("div",class_="summary_text").get_text().strip()
        movie_bio_lis.append(bio)
    # return(movie_bio_lis)
        main_genres=soup.find("div",class_="subtext")
        movie_genre=main_genres.find_all("a")
        genre_div=movie_genre.pop()
        time=main_genres.time.get_text().strip()
        for i in range(0,len(time)):
            movie_time=int(time[0])*60+int(time[3])
        runtime.append(movie_time)
    # return(runtime)
        genr_lis=[]
        for k in movie_genre:
            genr_lis.append(k.get_text())
        gener_movie.append(genr_lis)
    # return(gener_movie)
        div=soup.find("div",id="titleDetails",class_="article")
        text_blkk=div.find_all("div")

        for i in text_blkk:
            try:
                if "Country:" == i.find("h4").get_text():
                    Country = i.find("a").get_text()
                    country.append(Country)
                    # return Country
                elif "Language:" == i.find("h4").get_text():
                    Language = i.find("a").get_text()
                    language.append([Language])
            except:
                pass
        # country.append(Country)
        # language.append(Language)
    # return(country)
    # return(language)   
            
        dic={}
        for data in range(0,len(name_lis)):
            dic["name"]=name_lis[data]
            dic["director"]=director_nam_list[data]
            dic["poster_img_url"]=poster_img[data]
            dic["bio"]=movie_bio_lis[data]
            dic["runtime"]=runtime[data]
            dic["gener"]=gener_movie[data]
            dic["country"]=country[data]
            dic["language"]=language[data]
        ovreall_10_movie_detail.append(dic)


    return(ovreall_10_movie_detail)

overall=get_movie_list_details()

pprint.pprint(overall)