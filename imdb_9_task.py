from imdb_1_task import *
# from imdb_8_task import *
from imdb_4_task import *
import time
import random

def get_movie_list_details(data):
    # random_time=random.randint(1,3)
    detailed_Lis=[]
    for i in data[0:5]:
        url1=i["movie url"]


        random_time=random.randint(1,3)
        # url1=i["movie url"]
        time.sleep(random_time)
        time_taken=time.time()
        # print(time_taken)
        data=scrape_movie_details(url1)
        # scrape=scrape_movie_details(url1)
        # return(scrape)
        detailed_Lis.append(data)
    return(detailed_Lis)

movieDetail=get_movie_list_details(movie_details)


# pprint.pprint(movieDetail)

