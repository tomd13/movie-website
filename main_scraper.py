"""Scraper to get movie show times for Vue Cinema Wood Green from LondonNet.co.uk"""

from bs4 import BeautifulSoup
import requests


source = requests.get('http://www.londonnet.co.uk/cinema/vuewoodgreen.html').text
soup = BeautifulSoup(source, 'lxml')

first_week = soup.find('div', {'id': 'cin_starting_lastweek'})
second_week = soup.find('div', {'id': 'cin_starting_thisweek'})


def get_movies(week):
    """Return a dictionary of movies and times for a given week"""
    movies = {}
    for movie in week.find_all('div', class_='venuefilmbloc'):
        movies[movie.a.strong.text] = "\n".join(movie.span.text.split('; '))
    return movies

print(first_week.strong.text)
print(get_movies(first_week))
print(second_week.strong.text)
print(get_movies(second_week))
