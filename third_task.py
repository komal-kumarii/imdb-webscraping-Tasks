
from sec_task import  *
# pprint.pprint(year_details)
def group_by_decade(movies):
    year_decade=[]
    for k in movies:
        a=k %10
        decade=k-a
        if decade not in year_decade:
            year_decade.append(decade)
    year_decade.sort()
    # return(year_decade)
    dic={}
    # decades_movie=[]
    for i in year_decade:
        decade_key=i+9
        lis=[]
        for j in movies:
            # return(movies[i])
            if j>=i and j<=decade_key:
                for data in movies[j]:
                    if data not in lis:
                        lis.append(data)
        # return(lis)
        dic[i]=lis
        # return(dic)
                # if year_decade[i]>=s:
                    # lis.append(s)
        # dic[i]=lis
    return(dic)    

pprint.pprint(group_by_decade(year_details))