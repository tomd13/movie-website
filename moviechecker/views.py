from django.shortcuts import render
from main_scraper import get_movies
from .utils import get_movies
from bs4 import BeautifulSoup
import requests


def movie_list(request):
    source = requests.get('http://www.londonnet.co.uk/cinema/vuewoodgreen.html').text
    soup = BeautifulSoup(source, 'lxml')

    first_week = soup.find('div', {'id': 'cin_starting_lastweek'})
    second_week = soup.find('div', {'id': 'cin_starting_thisweek'})

    first_week_movies = get_movies(first_week)
    second_week_movies = get_movies(second_week)
    # first_week_movies = {'Incredibles 2': 'Fri/Sun 11:00 (Fri) 12:00 13:00 14:10 (Fri) 14:45 15:40 16:30 17:45'}
    # second_week_movies = {'Jurassic World: Fallen Kingdom': 'Sat 15:25 Sun 13:25 16:15 Mon 10:45 Thu 17:05'}

    return render(request, 'moviechecker/movie_list.html', {'first_week': first_week.strong.text,
                                                            'second_week': second_week.strong.text,
                                                            'first_week_movies': first_week_movies,
                                                            'second_week_movies': second_week_movies})
