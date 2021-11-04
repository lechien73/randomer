import requests
from bs4 import BeautifulSoup


def get_dilbert(strip_date):

    DILBERT_BASE = "https://dilbert.com/strip/"

    comic = {}

    r = requests.get(f"{DILBERT_BASE}{strip_date}")

    soup = BeautifulSoup(r.text, 'html.parser') 

    image = soup.find_all("img", attrs={"class": "img-comic"})
    title = soup.find_all("span", attrs={"class": "comic-title-name"})

    comic["url"] = image[0]["src"]
    comic["title"] = title[0].text

    return comic
