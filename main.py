from bs4 import BeautifulSoup
import requests
import openpyxl

# Scrape Amazon website
def web_scrape(search_query):
    url=f"https://www.amazon.co.uk/"
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
             }

# HTTP GET request to specified URL
response = requests.get(url, headers=headers)

# Check if request was successful

# parse HTML content and extract relevant data

# Extract information from search results

# Export data to Excel spreadsheet