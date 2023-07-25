import requests
from datetime import datetime
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def is_valid_format(str):
    try:
        datetime.strptime(str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def fetch_page(fdate):
    url = f'https://www.billboard.com/charts/hot-100/{fdate}/'
    response = requests.get(url)
    response_text = response.text
    return BeautifulSoup(response_text, 'html.parser')


#date = input("what year you would like to travel to in YYY-MM-DD format? ")
if is_valid_format("2022-07-24"):
    soup = fetch_page("2022-07-24")
    song_names_spans = soup.select("li ul li h3")
    song_names = [song.getText().strip() for song in song_names_spans]
    print(song_names)
else:
    print("Invalid date format, please try again")

