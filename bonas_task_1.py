from imdb_4_task import *

def similar_movie_list(movie_url):
    response=requests.get(movie_url)
    response_txt=response.text
    soup=BeautifulSoup(response_txt,"html.parser")
    # similar_movie=[]
    try:
        main = soup.find("div", class_="article", id = "titleRecs")
        for i in main:
            return(i)
    except:
        return("not found")
    # div = soup.find("div", class_="article", id = "titleRecs")
    #  = div.find("div", class_="rec_view")
    # page = div.find("div", class_="rec_page")
    # item_selected = div.findAll("div", class_= "rec_item")
    # # return(item_selected)
    # try:
        # for i in div:
            # a = i.find("a")
            # href = a.img["alt"]
            # pprint(i)
    # except :
        # pass
    #     similar_movies["scrape_movies"] = href 
    #     similar.append(similar_movies)
    
movie_url='https://www.imdb.com/title/tt0066763/'
pprint.pprint(similar_movie_list(movie_url))

