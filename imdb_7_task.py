from imdb_5_task import *

def analyse_movie_detail(overall_lis):
    dir_name=[]
    for i in overall_lis:
        # for dic in range(len(i)):
            # return(dic)
        dir_name.append(i["director"]) 
    # return(dir_name)
    a=[]
    for nam in range(0,len(dir_name)):
        for j in range(0,len(dir_name[nam])):
            a.append(dir_name[nam][j])
    # return(a)
    avoid_dup=[]
    for names in a:
        if names not in avoid_dup:
            avoid_dup.append(names)
    # return(avoid_dup)
    dic={}
    for uniq in avoid_dup:
        count=0
        for k in a:
            if uniq==k:
                count+=1
        dic[uniq]=count
    return(dic)
pprint.pprint(analyse_movie_detail(overall))