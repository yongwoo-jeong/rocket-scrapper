import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome('C:/Users/JYW/Desktop/chromedriver/chromedriver.exe')
phantom = webdriver.PhantomJS(r'/Users/JYW/Desktop/phantomjs/phantomjs.exe')

driver.implicitly_wait(3)
driver.get('https://www.rocketpunch.com/jobs?career_type=1&job=1&page=1')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')