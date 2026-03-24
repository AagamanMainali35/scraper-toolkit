from bs4 import BeautifulSoup
import requests

base_url = "https://books.toscrape.com/"
session = requests.Session()

def get_book_details(book_url):
    rq = session.get(book_url)
    bs = BeautifulSoup(rq.content, "lxml")

    data = {}

    product_div = bs.find("div", class_="product_main")
    if product_div:
        data["name"] = product_div.h1.text.strip()

    return data

def scrape():
    url = base_url
    rq = session.get(url)
    bs = BeautifulSoup(rq.content, "lxml")

    for article in bs.find_all("article", class_="product_pod"):
        relative_url = article.h3.a["href"]

        if relative_url.startswith("catalogue/"):
            book_url = f"{base_url}{relative_url}"
        else:
            book_url = f"{base_url}catalogue/{relative_url}"

        print(book_url)