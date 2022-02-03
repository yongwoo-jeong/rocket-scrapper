import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('C:/Users/JYW/Desktop/project/python/rocket_scrapper/chromedriver.exe')
phantom = webdriver.PhantomJS(r'/Users/JYW/Desktop/project/python/rocket_scrapper/phantomjs.exe')


def get_last_page():    
    driver.get('https://www.rocketpunch.com/jobs?career_type=1&job=1')
    element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'pagination')))
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    last_page_number = int(soup.select('div.pagination > div.computer > a')[5].get_text())
    return last_page_number

def extract_jobs(last_page):
    jobs = []
    for page in range(1, last_page + 1):
        print(f"Scraping Rocket-Punch Jobs for Junior: page: {page}")
        driver.get(f'https://www.rocketpunch.com/jobs?career_type=1&job=1&page={page}')
        element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'pagination')))
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        company_items = soup.select('div.company-list > div.company.item')
        for company_item in company_items:
            company_name = company_item.select_one('div.company-name > a > h4.name > strong').get_text()
            job = company_item.select_one('div.job-detail > div > a.job-title').get_text()
            career_info = company_item.select_one('span.job-stat-info').get_text()
            apply_link = company_item.select_one('div.job-detail > div > a')['href']
            apply_link = f"https://www.rocketpunch.com{apply_link}"
            jobs.append({'Company Name':company_name, 'Job':job, 'Career Info': career_info, 'Apply Link':apply_link})
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    driver.quit()
    return jobs

