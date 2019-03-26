import urllib.parse
import requests
import json
import urllib3
import csv

#movie_number_fightclub = '550' 
#movie_number_avengers_endgame = '299534'
#movie_number_the_avengers = '24428'
#page = '553'
#movie_list = ['550', '299534']
#main_api = 'https://api.themoviedb.org/3/movie/' + page +'?api_key=97a633aa203b7ca721c713787e00b365&language=en-US'

#url = main_api

#json_data = requests.get(url).json()
#print(json_data)

#id_movie = (json_data['id'])
#print()
#print("Id:", id_movie)

#title_movie = (json_data['original_title'])
#print("Title:", title_movie)

#poster_movie = (json_data['poster_path'])
#poster_url = 'https://image.tmdb.org/t/p/original{key}'.format(key=poster_movie)
#print("Poster:", poster_url)

#description_movie = (json_data['overview'])
#print("Description:", description_movie)

#pc = []
#for each in (json_data['production_companies']):
#    pc.append((each['name']))
    #print('Production Company Logo:', (each ['logo_path']))
    #print(pc)
    
#budget = (json_data['budget'])
#print("Budget:", budget)

#revenue = (json_data['revenue'])
##print("Revenue:", revenue)

#gm = []
#for each in (json_data['genres']):
#    gm.append((each['name']))
    #print(gm)

#release_date = (json_data['release_date'])
#print("Release Date:", release_date)

#tagline = (json_data['tagline'])
#print("Tagline:", tagline)

#status_movie = (json_data['status'])
#print("Status:", status_movie)

#imdb_movie_id = (json_data['imdb_id'])
#imdb_page = 'https://www.imdb.com/title/{key}'.format(key=imdb_movie_id)
#print("Imdb Website:", imdb_page)

pages = [str(i) for i in range(1000, 5000)]

with open('mycsv.csv', 'w', newline='', encoding="utf-8") as f:
    fieldnames = ['Id Movie', 'Title', 'Poster', 'Description', 'Genres' , 'Budget', 'Revenue', 'Release Date', 'Runtime', 'Tagline', 'Status', 'Imdb Website', 'Production Company', 'Vote Average', 'Vote Count', 'Backdrop Image']
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)

    thewriter.writeheader()

    for page in pages:
        new_api = 'https://api.themoviedb.org/3/movie/' + page +'?api_key=97a633aa203b7ca721c713787e00b365&language=en-US'
        url = new_api
        json_data = requests.get(url).json()
        #print(json_data)

        try:
            adult = (json_data['adult'])
            #print(adult)

            imdb_movie_id = (json_data['imdb_id'])
            #imdb_page = 'https://www.imdb.com/title/{key}'.format(key=imdb_movie_id)

            release_date = (json_data['release_date'])

            ori_language = (json_data['original_language'])
            #print(ori_language)

            #backdrop_image = (json_data['backdrop_path'])
            #print (backdrop_image)

            #lang_spoken = (json_data['spoken_languages'][0]['name'])
            #print (lang_spoken)
            # was added to the if statement: and str(lang_spoken) in ['en']

            if str(adult) in ['False'] and str(imdb_movie_id) is not '' and str(release_date) is not '' and str(release_date) >= '2000' and str(ori_language) in ['en']:
            #if str(adult) in ['False']:

                id_movie = (json_data['id'])
                title_movie = (json_data['original_title'])

                poster_movie = (json_data['poster_path'])
                poster_url = 'https://image.tmdb.org/t/p/original{key}'.format(key=poster_movie)

                description_movie = (json_data['overview'])

                pc = []
                for each in (json_data['production_companies']):
                    pc.append((each['name']))
                    
                budget = (json_data['budget'])

                revenue = (json_data['revenue'])

                gm = []
                for each in (json_data['genres']):
                    gm.append((each['name']))

                #release_date = (json_data['release_date'])

                runtime = (json_data['runtime'])

                tagline = (json_data['tagline'])

                status_movie = (json_data['status'])

                #imdb_movie_id = (json_data['imdb_id'])
                imdb_page = 'https://www.imdb.com/title/{key}'.format(key=imdb_movie_id)

                vote_average = (json_data['vote_average'])

                vote_count = (json_data['vote_count'])

                backdrop_image = (json_data['backdrop_path'])
                backdrop_url = 'https://image.tmdb.org/t/p/original{key}'.format(key=backdrop_image)

                print(id_movie,'movie printed')
                thewriter.writerow({'Id Movie' : id_movie, 'Title' : title_movie, 'Poster' : poster_url, 'Description': description_movie, 'Genres': gm, 'Budget' : budget, 'Revenue' : revenue, 'Release Date': release_date, 'Runtime': runtime, 'Tagline': tagline, 'Status': status_movie, 'Imdb Website': imdb_page, 'Production Company':pc, 'Vote Average': vote_average, 'Vote Count': vote_count, 'Backdrop Image': backdrop_url})
            else:
                print ('Adult Film | No Imdb Website | No Release Date | Movie Released Before Year 2000 | Original Language Not English')
        except KeyError:
            print ("id does not exist")
            pass