import urllib.request
import json


def get_movies(week):
    """Return a dictionary of movies and times for a given week"""
    movies = {}
    for movie in week.find_all('div', class_='venuefilmbloc'):
        movies[movie.a.strong.text] = "\n".join(movie.span.text.split('; '))
    return movies


def get_omdb_data(movie, year):
    url = f'http://www.omdbapi.com/?t={movie.replace(" ", "+")}&y={year}&apikey=3bcfb0a5'
    return json.load(urllib.request.urlopen(url))
