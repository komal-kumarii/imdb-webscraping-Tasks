from imdb_1_task import *
from imdb_4_task import *
from imdb_9_task import *

def analyse_language_and_directors(moviedetails):
    # for i in range(0,len(moviedetails)):
        # url=(moviedetails[i]["movie url"])
        # data=scrape_movie_details(url)
    director_dict={}
    for movies in moviedetails:
        # return(movies)
        for director in movies["Director"]:
            # print(director)
            director_dict[director]={}
    for i in range(0,len(moviedetails)):
        for director in director_dict:
            if director in moviedetails[i]["Director"]:
                count=0
                for languages in moviedetails[i]["language"]:
                    # a={languages,0}
                    # print(languages)
                    # count+=1
                    director_dict[director][languages]=count
    for i in range(0,len(moviedetails)):
        for director in director_dict:
            if director in moviedetails[i]["Director"]:
                # count=0
                for languages in moviedetails[i]["language"]:
                    director_dict[director][languages]+=1


    return(director_dict)

movieDetail=get_movie_list_details(movie_details)

pprint.pprint(analyse_language_and_directors(movieDetail))
# pprint.pprint(movieDetail)