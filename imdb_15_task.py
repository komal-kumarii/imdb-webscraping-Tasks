from imdb_1_task import  *
from imdb_12_task import  *

def analyse_actors(movie_list):
    all_names=[]
    uniq_name=[]
    all_ids=[]
    uniq_ids=[]
    main_dic={}
    for movies in range(10,15):
        # return(movies["movie url"])
        # return(movies)
        casting=scrape_movie_cast(movie_list[movies]["movie url"])
        for info in casting:
            all_names.append(info["name"])
    # return(all_names)
            # imdb=(info["imdb_id_no."])
            all_ids.append(info["imdb_id_no."])
        for nam in all_names:
            if nam not in uniq_name:
                uniq_name.append(nam)
        for ids in all_ids:
            if ids not in uniq_ids:
                uniq_ids.append(ids)
        
    for k in range(0,len(uniq_name)):
        main_dic[uniq_ids[k]]={}
        # return(main_dic)
        # main_dic[k]["imdb_id_no."]={}
        count=0
        d={}
        for j in all_names:
            if uniq_name[k] ==j:
                count+=1
        d["name"]=uniq_name[k]
        d["num_movies"]=count
        # print(d)
        main_dic[uniq_ids[k]] =  d
    return(main_dic)
pprint.pprint(analyse_actors(movie_details))