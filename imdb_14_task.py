from imdb_12_task import  *
from imdb_1_task import  *

def  analyse_co_actors(movie_list):
    main_lead=[]
    co_lead=[]
    uniq_co_lead=[]
    main_lead_id=[]
    co_lead_id=[]
    main_dics={}
    num_count=[]
    for movies in range(11,20):
        url_s=(movie_list[movies]["movie url"])
        casting=scrape_movie_cast(url_s)
        # for j in range(0,len(casting)):
        main_lead.append(casting[0]["name"])
        main_lead_id.append(casting[0]["imdb_id_no."])
        co_lead.append(casting[1]["name"])
        co_lead_id.append(casting[1]["imdb_id_no."])
    # print(co_lead)
    for s in co_lead:
        if s not in uniq_co_lead:
            uniq_co_lead.append(s)
    for nam in uniq_co_lead:
        count=0
        for n in co_lead:
            if nam==n:
                count+=1
        num_count.append(count)

    for k in range(0,len(main_lead)):
        main_dics[main_lead_id[k]]={}
        d={}
        lis=[]
        nest_dic={}
        # d["name"]=main_lead[k]
        # d["frequenr co-factors"]={}
        nest_dic["name"]=co_lead[k]
        nest_dic["imdb_no."]=co_lead_id[k]
        nest_dic["num_movies"]=num_count[k]
        lis.append(nest_dic)
        # return(lis)
        d["name"]=main_lead[k]
        d["frequenr co-factors"]=lis
        # print(d)
        main_dics[main_lead_id[k]] =  d
    return(main_dics)
pprint.pprint(analyse_co_actors(movie_details))
