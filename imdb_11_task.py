from imdb_4_task import *
from imdb_9_task import *

def analyse_movies_genre(data):
    # return(data)
    genere_movie=[]
    for movies in data:
        for gen in movies['genre']:
            genere_movie.append(gen)
    # return(genere_movie)
    single_genre=[]
    for i in genere_movie:
        if i not in single_genre:
            single_genre.append(i)
    # return(single_genre)
    genere={}
    for item in single_genre:
        count=0
        for k in genere_movie:
            if item==k:
                count+=1
        genere[item]=count
    return(genere)

pprint.pprint(analyse_movies_genre(movieDetail))
