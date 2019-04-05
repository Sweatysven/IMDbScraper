import csv
from collections import defaultdict
import urllib.request
from urllib.error import HTTPError
from urllib.request import urlretrieve
import requests

with open('db_movies2.csv', encoding="utf-8") as csvfile:
    csvrows = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvrows:
        filename = row[0]+'b.jpg'
        url = row[15]
        print(filename + ' | ' + url)
        result = requests.get(url, stream=True)
        if result.status_code == 200:
            image = result.raw.read()
            open(filename,"wb").write(image)



