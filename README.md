
# Book Scraper for proshore Nepal

Date: 2026 , March 24th .

Project Description : This Python script is built for scrapping books from [https://books.toscrape.com/](https://books.toscrape.com/) and saves all the scrapped data as a `JSON file`. The scraper collects details that are mentioned below :

  * Name
  * Description
  * Price (including tax)
  * Tax
  * Availability
  * UPC
  * URL
  * Scraping date

## Requirements

* The script uses Python 3.11.3 as the python version
* The Libraries installed in this projects are:

  * `requests` for content fetch
  * `beautifulsoup4` as the default Web Scraping Library
  * `lxml` for Faster data parsing compared to `html.parser`


 The script will run and scrape all books information and save the data to `Books.json` file.

## Output

* **Books.json**: Contains a list of all books with their details. Example entry:

```
{
    "name": "A Light in the Attic",
    "description": "It's hard to imagine a world without A Light in the Attic...",
    "price": "£51.77",
    "tax": "£0.00",
    "availability": "In stock (22 available)",
    "upc": "a897fe39b1053632",
    "url": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "scrape_date": "2026-03-24"
}
```

## Performance
```
Total books: 1000
Time taken: 290.45 seconds to 330 seconds [Range might defer as per internet connection]
```



