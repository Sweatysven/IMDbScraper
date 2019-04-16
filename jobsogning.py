from requests import get
import urllib3
import csv
from bs4 import BeautifulSoup

# Get the URl set in place
url = 'https://graduateland.com/da/jobs/praktikpladser'
response = get(url)

# Get Status Code, if = 200, the website is live and working, ready to be scraped
print("Status Code:",response.status_code)

# Get the first 500 lines of the HTML source code
#print(response.text[:500])

# set up a working varibale html_soup, meaning we can scrape our html with Bs4
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

# find all posts
posts = html_soup.find_all('div', class_ = 'box-item--full-box-animated')
#print(postings)

# get first post
first_post = posts[0]
#print(first_post)

first_post_title = first_post.h3.text.strip()
print(first_post_title)

first_post_position = first_post.p.text.strip().replace("\n","")
print(first_post_position)

first_post_city = first_post.find('div', class_ = 'city').text.strip().replace("\r","")
print(first_post_city)

first_post_desc = first_post.find('div', class_ = 'description').text.strip().replace("\r","")
print(first_post_desc)

# Open a new link
# https://hackersandslackers.com/scraping-urls-with-beautifulsoup/