import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('C:/Users/JYW/Desktop/chromedriver/chromedriver.exe')
phantom = webdriver.PhantomJS(r'/Users/JYW/Desktop/phantomjs/phantomjs.exe')


driver.get('https://www.rocketpunch.com/jobs?career_type=1&job=1&page=1')
element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'pagination')))
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

def get_last_page():    
    last_page_number = int(soup.select('div.pagination > div.computer > a')[5].get_text())
    print(list(range(1, last_page_number + 1)))

get_last_page()