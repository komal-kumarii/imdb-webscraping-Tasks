
from imdb_1_task import  *
# pprint.pprint(movie_details)

def group_by_year(movies):
    year_info=[]
    empty_dic={}
    for i in range(len(movies)):
        if movies[i]['release year'] not in year_info:
        # info=movies[i]['release year']
            year_info.append(movies[i]['release year'])
    # return(year_info)
    for j in (year_info):
        lis=[]
        for k in range(0,len(movies)):
            if j == movies[k]["release year"]:
                    # return(movies[k])
                lis.append(movies[k])
        # r.append(lis)
    # return(r)
        empty_dic[j]=lis
    return(empty_dic)
    
year_details=(group_by_year(movie_details))

# pprint.pprint(year_details)
