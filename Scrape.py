from bs4 import BeautifulSoup
import requests

base_url = "https://books.toscrape.com/"
session = requests.Session()
book_data = []

def get_book_details(book_url):
    rq = session.get(book_url)
    bs = BeautifulSoup(rq.content, "lxml")

    data = {}

    product_div = bs.find("div", class_="product_main")
    if product_div:
        data["name"] = product_div.h1.text.strip()

        desc = bs.find("div", id="product_description")
        if desc:
            p = desc.find_next_sibling("p")
            if p:
                data["description"] = p.text.strip()
        else:
            data["description"] = ""

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

        details = get_book_details(book_url)
        details["url"] = book_url
        book_data.append(details)

scrape()
print(len(book_data))