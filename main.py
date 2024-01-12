from urllib.request import urlopen
from bs4 import BeautifulSoup

page = urlopen("https://weimergeeks.com/examples/scraping/example1.html")
soup = BeautifulSoup(page, "html.parser")
heading = soup.h1
print(heading.text)
city_list = soup.find_all("td", class_="city")
for city in city_list:
    print(city.get_text())