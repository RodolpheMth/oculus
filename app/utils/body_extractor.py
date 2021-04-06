import spacy
from spacy.lang.en.examples import sentences
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd

from resources.const import *

list_date = []
list_body = []
list_title = []
list_name = []
list_investor = []

def body_extractor(str_url):

    driver = webdriver.Chrome(executable_path=r'C:\webdrivers\chromedriver.exe')
    sleep(1)
    driver.get(str_url)
    try:
        element = driver.find_element_by_class_name('btn.primary')
    except:
        element = 0

    if element != 0:
        driver.execute_script("arguments[0].scrollIntoView();", element)
        driver.execute_script("arguments[0].click();", element)

        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')

        try:
            body = soup.find('div', attrs = {'class': 'article-content'}).text
        except:
            body = ""
        
        try:
            date = soup.find('time')['datetime']
        except:
            date = ""
        
        try:
            title = soup.find('h1', {'class': 'article__title'}).text
        except:
            title = ""
        
        try:
            investor = [ent.text.strip() for ent in nlp(soup.text).ents if ent.label_ in ["ORG"]]
        # spacy_labels_companies = [ent.text.strip() for ent in nlp(soup.text).ents if ent.label_ in ["ORG"]]
        # name = soup.find('a', href=True).text
        # if name:
        #     name_company = name
        # elif spacy_labels_companies:
        #     name_company = spacy_labels_companies
        # else:
        #     name_company = ""
        except:
            investor = ""

        
        try:
            spacy_labels_companies = [ent.text.strip() for ent in nlp(soup.find('h1', {'class': 'article__title'}).text).ents if ent.label_ in ["ORG", "PERSON"]]
            name_company = spacy_labels_companies
        except:
            name_company = ""
        
        list_date.append(date)
        list_body.append(body)
        list_title.append(title)
        list_name.append(name_company)
        list_investor.append(investor)
        
    return list_date, list_title, list_body, list_name, list_investor