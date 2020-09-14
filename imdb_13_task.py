from imdb_4_task import *
from imdb_12_task import *

def scrap_movie_cast(url):
    data = scrape_movie_details(url)
    # return(data)
    casting=scrape_movie_cast(url+"fullcredits?ref_=tt_cl_sm#cast")
    data["cast"]=casting
    # dic.update(casting)
    return(data)


url1='https://www.imdb.com/title/tt0066763/'
pprint.pprint(scrap_movie_cast(url1))
