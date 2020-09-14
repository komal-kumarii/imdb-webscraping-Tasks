from imdb_5_task import  *

def analyse_movie_by_language(language_lis):
    # return(language_lis)
    lang_value=[]
    for i in language_lis:
        # print(i["language"])
        if i["language"] not in lang_value:
            lang_value.append(i["language"])
    # return(lang_value)
    language_dic={}
    for index in lang_value:
        count=0
        for j in language_lis:
            if index==j["language"]:
                count+=1
        language_dic[index]=count
    return(language_dic)
pprint.pprint(analyse_movie_by_language(overall))