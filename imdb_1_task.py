import requests
from bs4 import BeautifulSoup
import re
import pprint

url=" https://www.imdb.com/india/top-rated-indian-movies/"
response=requests.get(url)
response_txt=response.text
# return(response_txt)
soup=BeautifulSoup(response_txt,"html.parser")		
	# return(soups)
def scrape_top_list():

	main_div=soup.find("div",class_="lister")
	t_body=main_div.find("tbody",class_="lister-list")
	trs=t_body.find_all("tr")
	
	movie_name=[]
	release_year=[]
	movie_position=[]
	rating=[]
	movie_url=[]
	movie_information=[]
	# dict={}
	our_list=["name","position","rating"," release year","url"]
	for tr in trs:
		value=tr.find("td",class_="titleColumn").get_text().strip()
		# return (value)
		postion_rank=''
		for i in value:
			if '.' not in i:
				postion_rank=postion_rank+i
				# movie_position.append(postion_rank)
			else:
				break
		movie_position.append(int(postion_rank))
	# return(movie_position)
		name=tr.find("td",class_="titleColumn").a.get_text().strip()
		movie_name.append(name)
	# return(movie_name)
		movie_rating=tr.find("td",class_="ratingColumn imdbRating").get_text().strip()
		rating.append(float(movie_rating))
	# return(rating)
		year=tr.find("td",class_="titleColumn")
		movie_year=year.find("span",class_="secondaryInfo").get_text()
		movie_year=re.sub('\((\d+)\)',r'\1',movie_year)
		# return(int(movie_year))
		release_year.append(int(movie_year))
		# return(release_year)
		urls=tr.find("td",class_="titleColumn")
		link=urls.a["href"]
		movie_link="https://www.imdb.com/"+link
		movie_url.append(movie_link)
	# return(movie_url)
		for i in range(0,len(movie_name)):
			dict={}
			dict["name"]=movie_name[i]
			dict["position"]=movie_position[i]
			dict["rating"]=rating[i]
			dict["release year"]=release_year[i]
			dict["movie url"]=movie_url[i]
		movie_information.append(dict)

	return(movie_information)
movie_details=(scrape_top_list())
# pprint.pprint(movie_details)
 
