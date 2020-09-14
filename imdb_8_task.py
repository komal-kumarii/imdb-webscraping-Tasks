from imdb_1_task import  *
import os 
import json

def scrape_movie_details(url):
    main_link=""
    for i in range(28,len(url)):
        if "/" != url[i]:
            main_link+=url[i]
        else:
            break
    # return(main_link)
    file_name=main_link+".json"
    # return(file_name)
    text_exist=None
    if os.path.exists(file_name)==True:
        read_file= open(file_name,"r")
        read=read_file.read()
        # print("okk")
        return read

    response=requests.get(url)
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
        
    url=soup.find("div",class_="slate_wrapper")
    url_div=url.find("div",class_="poster").img["src"]
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
    all_divs=article.find_all("div")
    value_lis=[]
    # movie_detalis_dict={}
    for t in range(0,4):
        country=(all_divs[t]).a.get_text()
        # return(country)
        value_lis.append(country)
    # return(value_lis)
    movie_detalis_dict={}
    movie_detalis_dict["name"]=movieName
    movie_detalis_dict[director]=direct_name
    movie_detalis_dict["poster_img_url"]=url_div
    movie_detalis_dict["country"]=value_lis[0]
    movie_detalis_dict["language"]=value_lis[1]
    movie_detalis_dict["bio"]=movie_bio
    movie_detalis_dict["runtime"]=movie_time
    movie_detalis_dict["genre"]=genr_lis

    my_file=open(file_name,"w")
    data=json.dumps(movie_detalis_dict)
    my_file.write(data)
    my_file.close()


    return(movie_detalis_dict)
url1=movie_details[0]["movie url"]
movie_list_detail=(scrape_movie_details(url1))

# pprint.pprint (movie_list_detail)


