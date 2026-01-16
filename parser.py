from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options


def parse_data(genres):
    driver = webdriver.Chrome()
    driver.minimize_window()
    driver.get(url=f'https://www.imdb.com/chart/top/?genres={genres}')
    names = driver.find_elements(By.CLASS_NAME, 'ipc-title__text')[:-1]
    info = ""
    for i in names:
        info += f'{i.text}\n\n'
    return info


'''
py -m venv venv
.\venv\Scripts\activate
py -m pip install --upgrade pip
pip install pytelegrambotapi
pip install selenium


'''