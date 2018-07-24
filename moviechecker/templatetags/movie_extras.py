from django.template.defaulttags import register
import urllib.request
import json


@register.filter
def get_times(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_rt(movie):
    url = f'http://www.omdbapi.com/?t={movie.replace(" ", "+")}&y=2018&apikey=3bcfb0a5'
    try:
        rt = json.load(urllib.request.urlopen(url))['Ratings'][1]['Value']
    except Exception:
        rt = ""
    return rt


@register.filter
def get_runtime(movie):
    url = f'http://www.omdbapi.com/?t={movie.replace(" ", "+")}&y=2018&apikey=3bcfb0a5'
    try:
        runtime = json.load(urllib.request.urlopen(url))['Runtime']
    except Exception:
        runtime = ""
    return runtime