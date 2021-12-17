from bs4 import BeautifulSoup
import requests,json
from pprint import pprint
def scrape_top_list():
	main_url = requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
	soup = BeautifulSoup(main_url.text,"html.parser")
	lister_list = soup.find("tbody", class_ = "lister-list")
	all_trs = lister_list.find_all("tr")
	movie_data = {}
	lists_of_movie = []
	position = 0
	# for the find teble data from table_row
	for td_data in all_trs :
		position = position + 1
		movie_data["position"] = position
		movie_data["name"] = td_data.find("td",class_="titleColumn").a.get_text()
		movie_data["year"] = (int(td_data.find("td",class_="titleColumn").span.get_text()[1:5]))
		movie_data["ratings"] = (float(td_data.find("td",class_="ratingColumn imdbRating").strong.get_text()[1:3]))
		urls = td_data.find("td",class_="titleColumn").a["href"]
		movie_data["urls"] = 'https://www.imdb.com'+urls[:17]
		lists_of_movie.append(movie_data.copy())
	# for make the file in our directory and dump the all collection data in that file.
	with open("geetu.json","w") as file :
		data = json.dumps(lists_of_movie,indent=4, sort_keys = True)
		file.write(data)
	return (lists_of_movie)
print (scrape_top_list())