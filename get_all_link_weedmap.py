import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, executable_path="F:\\Selenium\\chromedriver.exe")

driver.get('https://weedmaps.com/dispensaries/harmony-dispensary?filter%5BanyCategories%5D%5B%5D=flower')


list = []
list1=[]
list2=[]
list3=[]
visited=[]
page = 2
while page <= 7:

    blocks = driver.find_elements(By.CLASS_NAME,"lloEgg")
    for block in blocks:
        element = block.find_elements(By.TAG_NAME,"a")
        for el in element:
            list.append(el.get_attribute("href"))
            print(list)
    blocksss = driver.find_elements(By.CLASS_NAME,'kmGAHV')
    for blockss in blocksss:
        block = blockss.find_elements(By.CLASS_NAME,'cVQPKf')
    for href in block:
        list2.append(href.get_attribute("href"))
        print(list2)
    driver.get(list2[1])
    list2=[]
    list=[]

driver.quit()


