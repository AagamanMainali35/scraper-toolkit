from bs4 import BeautifulSoup
import requests

base_url = "https://books.toscrape.com/"
session = requests.Session()

def scrape():
    url = base_url
    rq = session.get(url)
    bs = BeautifulSoup(rq.content, "lxml")