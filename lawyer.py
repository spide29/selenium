# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# from selenium.common.exceptions import NoSuchElementException
# import sqlite3
# import requests
# from bs4 import BeautifulSoup

# options = webdriver.ChromeOptions() 
# options.add_argument("start-maximized")
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options, executable_path="F:\\1.2 MIT Django Project\\chromedriver.exe")
# driver.get('https://lso.ca/public-resources/finding-a-lawyer-or-paralegal/directory-search/results')

# time.sleep(10)
# list = []
# list1=[]
# list2=[]
# list3=[]
# visited=[]
# while True:
#     blocks = driver.find_elements(By.CLASS_NAME,"member-listing-name")
#     for block in blocks:
#         element = block.find_elements(By.TAG_NAME,"a")
#         for el in element:
#             list.append(el.get_attribute("href"))
#             print(list)
#     for link in list:
#         if link not in visited:
#             visited.append(link)
#             response = requests.get(link)
#             soup = BeautifulSoup(response.content, 'html.parser')
#             name = soup.find('h2', {'class': 'member-name-primary'}).text
#             list2.append(name)
#             print(name)
#     button =driver.find_element(By.XPATH, '//*[@id="content-wrapper"]/div[1]/section/div/div[2]/div[2]/div[2]/div[3]/button')
#     button.click()
#     time.sleep(5)
#     list=[]

# driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import sqlite3
import requests
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, executable_path="F:\\Selenium\\chromedriver.exe")

driver.get('https://lso.ca/public-resources/finding-a-lawyer-or-paralegal/directory-search/results')

time.sleep(10)
list1 = []
list2 = []
list3 = []
visited = []

while True:
    blocks = driver.find_elements(By.CLASS_NAME, "member-listing-name")
    for block in blocks:
        element = block.find_elements(By.TAG_NAME, "a")
        for el in element:
            list1.append(el.get_attribute("href"))
            print(list1)
    for link in list1:
        if link not in visited:
            visited.append(link)
            response = requests.get(link)
            soup = BeautifulSoup(response.content, 'html.parser')
            # name = soup.find("h2").text
            # list3.append(name)
            # print(name)

            for div in soup.find_all('div', {'class': 'member-info-value'}):
                span = div.find_all('span')
                value = div.get_text().strip()
                list2.append(value)
                print(value)
            

    button = driver.find_element(By.XPATH, '//*[@id="content-wrapper"]/div[1]/section/div/div[2]/div[2]/div[2]/div[3]/button')
    button.click()
    time.sleep(10)
    list1=[]
    
driver.quit()
