import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('C:/Users/JYW/Desktop/chromedriver/chromedriver.exe')
phantom = webdriver.PhantomJS(r'/Users/JYW/Desktop/phantomjs/phantomjs.exe')


driver.get('https://www.rocketpunch.com/jobs?career_type=1&job=1')
element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'pagination')))
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

def get_last_page():    
    last_page_number = int(soup.select('div.pagination > div.computer > a')[5].get_text())
    return last_page_number

def extract_jobs(last_page):
    for page in range(1, last_page + 1):
        print(f"Scraping Rocket-Punch Jobs for Junior: page: {page}")
        driver.get(f'https://www.rocketpunch.com/jobs?career_type=1&job=1&page={page}')
        company_items = soup.select('div#company-list > div.company.item')
        for company_item in company_items:
            company = company_item.select_one('div.company-name > a > h4.name > strong').get_text()
            job = company_item.select_one('div.job-detail > div > a.job-title').get_text()
            career_info = company_item.select_one('span.job-stat').get_text()
            apply_link = company_item.select_one('div.job-detail > div > a')
        '''
        for company_item in company_items:
            company = soup.select_one('div.company-name > a > h4.name > strong').get_text()
            job = soup.select_one('div.job-detail > div > a.job-title').get_text()
            print(company, job)
        companies = soup.select('div.company-name > a > h4.name > strong')
        for company in companies:
            company = company.get_text()
        jobs = soup.select('div.job-detail > div > a.job-title')
        for job in jobs:
            job = job.get_text()
        '''

extract_jobs(1)