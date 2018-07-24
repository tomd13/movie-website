from bs4 import BeautifulSoup
from selenium import webdriver
import requests


browser = webdriver.Chrome()
browser.get("https://www.myvue.com/cinema/wood-green/whats-on/")
innerHTML = browser.execute_script("return document.body.innerHTML")


#source = requests.get('https://www.myvue.com/cinema/wood-green/whats-on/').text

soup = BeautifulSoup(innerHTML, 'lxml')

for movie in soup.find_all('div', class_='filmlist__item'):
    print(movie.find('div', class_='filmlist__info').a.span.get_text(strip=True))
