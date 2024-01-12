from urllib.request import urlopen
from bs4 import BeautifulSoup

page = urlopen("https://weimergeeks.com/examples/scraping/example1.html")
soup = BeautifulSoup(page, "html.parser")
heading = soup.h1
print(heading.text)
