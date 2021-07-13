import requests
from bs4 import BeautifulSoup

page_count = 88
URL = f"https://www.rocketpunch.com/jobs?career_type=1&job=1&page=1"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find_all("div", {"class":"floated"})
    #pages = pagination.find_all("a")
    print(soup)

get_last_page()