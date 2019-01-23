from requests import get
from bs4 import BeautifulSoup
import pandas as pd
from warnings import warn
from IPython.core.display import clear_output
from time import time
from time import sleep
from random import randint

url = 'https://www.imdb.com/search/title?release_date=2017-01-01,2017-12-31&sort=num_votes,desc'

response = get(url)
#print(response.text[:500])

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
#print(type(movie_containers))
#print(len(movie_containers))

first_movie = movie_containers[0]
#print(first_movie.h3.a)

first_name = first_movie.h3.a.text
print(first_name)

first_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold')
#print(first_year)

first_year = first_year.text
print(first_year)

first_imdb = float(first_movie.strong.text)
print(first_imdb)

#first_mscore = first_movie.find('span', class_ = 'metascore favorable')
#first_mscore = int(first_mscore.text)
#print(first_mscore)

# Lists to store the scraped data in
names = []
years = []
imdb_ratings = []
#metascores = []
#votes = []

# Preparing the monitoring of the loop
start_time = time()
requests = 0
headers = {"Accept-Language": "en-US, en;q=0.5"}
pages = [str(i) for i in range(1,501,50)]
years_url = [str(i) for i in range(2010,2018)]

# For every year in the interval 2000-2018
for year_url in years_url:

    # For every page in the interval 1-4
    for page in pages:

        # Make a get request
        response = get('http://www.imdb.com/search/title?release_date=' + year_url +  
        '&sort=num_votes,desc&start=' + page + '&ref_=adv_nxt', headers = headers)

        # Pause the loop
        sleep(randint(8,15))

        # Monitor the requests
        requests += 1
        elapsed_time = time() - start_time
        print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
        clear_output(wait = True)

        # Throw a warning for non-200 status codes
        if response.status_code != 200:
            warn('Request: {}; Status code: {}'.format(requests, response.status_code))

        # Break the loop if the number of requests is greater than expected
        if requests > 72:
            warn('Number of requests was greater than expected.')  
            break
        
        # Parse the content of the request with BeautifulSoup
        page_html = BeautifulSoup(response.text, 'html.parser')

        # Select all the 50 movie containers from a single page
        mv_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')

        # For every movie of these 50
        for container in mv_containers:
            # Scrape the name
            name = container.h3.a.text
            names.append(name)

            # Scrape the year 
            year = container.h3.find('span', class_ = 'lister-item-year').text
            years.append(year)

            # Scrape the IMDB rating
            imdb = float(container.strong.text)
            imdb_ratings.append(imdb)

movie_ratings = pd.DataFrame({'movie': names,
                              'year': years,
                              'imdb': imdb_ratings})

movie_ratings = movie_ratings[['movie', 'year', 'imdb']]
movie_ratings.head()

movie_ratings.to_csv('movie_ratings1.csv')

    





