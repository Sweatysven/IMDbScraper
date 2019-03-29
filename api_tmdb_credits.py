import urllib.parse
import requests
import json
import urllib3
import csv

page = '27205'
new_api = 'https://api.themoviedb.org/3/movie/' + page +'/credits?api_key=97a633aa203b7ca721c713787e00b365'
url = new_api
json_data = requests.get(url).json()
#print(json_data)

id_movie = (json_data['id'])
print(id_movie)

cast = []
for each in (json_data['cast']):
    cast.append((each['name']))
#print(cast)

character = []
for each in (json_data['cast']):
    character.append((each['character']))

for i in range(20):
    ca = cast[i]
    ch = character[i]
    result = ca +': '+ ch
print(result)

