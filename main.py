from bs4 import BeautifulSoup
import requests

url = "https://weimergeeks.com/examples/scraping/example1.html"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
cities = soup.select('td.city')
for city in cities:
    print(city.text)