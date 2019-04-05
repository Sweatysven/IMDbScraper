import csv
from collections import defaultdict
import urllib.request
from urllib.error import HTTPError
from urllib.request import urlretrieve
import requests

columns = defaultdict(list) # each value in each column is appended to a list

with open('mycsv4.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
            # based on column name k

poster_url = (columns['Poster'])
backdrop_url = (columns['Backdrop Image'])
#print (backdrop_url)
#print (poster_url)

#for index, url in enumerate(poster_url):

with open('mycsv4.csv') as csvfile:
    csvrows = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvrows:
        filename = row[0]+'.jpg'
        url = row[2]
        print(url)
        result = requests.get(url, stream=True)
        if result.status_code == 200:
            image = result.raw.read()
            open(filename,"wb").write(image)



