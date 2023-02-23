# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# from selenium.common.exceptions import NoSuchElementException


# options = webdriver.ChromeOptions() 
# options.add_argument("start-maximized")
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options, executable_path="F:\\Selenium\\chromedriver.exe")
# driver.get('https://weedmaps.com/dispensaries/in/united-states/california/lake-forest')

# links = []
# title=[]
# star=[]
# raiting=[]
# medical=[]
# purchesh=[]
# phone=[]

# div = driver.find_elements(By.CLASS_NAME, 'eQOCGV')
# for d in div:
#     link_els = d.find_elements(By.TAG_NAME, 'a')
#     for link_el in link_els:
#         href = link_el.get_attribute('href')
#         links.append(href)

# for link in links:
#     driver.get(link)
#     h1 = driver.find_elements(By.TAG_NAME,"h1")
#     for h in h1:
#         # title.append(h.text)
#         print(h.text)

#     div = driver.find_elements(By.CLASS_NAME,'eFswmm')
#     for di in div:
#         d = di.find_element(By.CLASS_NAME,'lgnROl')
#         # star.append(d.text)
#         print(d.text)


#     div = driver.find_elements(By.CLASS_NAME,'eFswmm')
#     for di in div:
#         d = di.find_element(By.CLASS_NAME,'gcZZKx')
#         # raiting.append(d.text)
#         print(d.text)

    
#     h1 = driver.find_elements(By.XPATH,'//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[3]/div')
#     for h in h1:  
#         # medical.append(h.text)
#         print(h.text)

    
#     h1 = driver.find_elements(By.XPATH,'//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[5]')
#     for h in h1:
#         # purchesh.append(h.text)
#         print(h.text)

   
#     h1 = driver.find_elements(By.XPATH,'//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[4]/div/div[3]/a[1]/div[2]')
#     for h in h1:
#         # phone.append(h.text)
#         print(h.text)

# # data = {"Title": title, "Star": star, "Rating":raiting , "Type": medical,"purchesh": purchesh,"Phoneno": phone }
# # df = pd.DataFrame(data)
# # with pd.ExcelWriter("data.xlsx") as writer:
# #     df.to_excel(writer, index=False) 
   
# driver.quit()

############################################################################################################

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import sqlite3

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, executable_path="F:\\Selenium\\chromedriver.exe")
driver.get('https://weedmaps.com/dispensaries/in/united-states/california/lake-forest')

links = []
disp=[]
temp=[]
vvisited=[]
h1_list = []
price_list = []

while True:
    div = driver.find_elements(By.CLASS_NAME, 'eQOCGV')
    for d in div:
        link_els = d.find_elements(By.TAG_NAME, 'a')
        for link_el in link_els:
            href = link_el.get_attribute('href')
            disp.append(href)
            
    blocksss = driver.find_elements(By.CLASS_NAME,'kmGAHV')
    for blockss in blocksss:
        block = blockss.find_elements(By.CLASS_NAME,'cVQPKf')
    for href in block:
        temp.append(href.get_attribute("href"))
        
    if temp[1] is None:
        temp=[]
        vvisited.extend(disp)
        disp=[]
        break

    else:
        driver.get(temp[1])
        temp=[]
        vvisited.extend(disp)
        disp=[]
for links in vvisited:
    driver.get(links)
    h1 = driver.find_elements(By.TAG_NAME,"h1")
    for h in h1:
        # title.append(h.text)
        print(h.text)

    div = driver.find_elements(By.CLASS_NAME,'eFswmm')
    for di in div:
        d = di.find_element(By.CLASS_NAME,'lgnROl')
        # star.append(d.text)
        print(d.text)

    div = driver.find_elements(By.CLASS_NAME,'eFswmm')
    for di in div:
        d = di.find_element(By.CLASS_NAME,'gcZZKx')
        # raiting.append(d.text)
        print(d.text)
    
    h1 = driver.find_elements(By.XPATH,'//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[3]/div')
    for h in h1:  
        # medical.append(h.text)
        print(h.text)

    h1 = driver.find_elements(By.XPATH,'//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[1]')
    for h in h1:  
        # medical.append(h.text)
        print(h.text)

    h1 = driver.find_elements(By.XPATH,'//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[5]')
    for h in h1:
        # purchesh.append(h.text)
        print(h.text)

    h1 = driver.find_elements(By.XPATH,'//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[4]/div/div[3]/a[1]/div[2]')
    for h in h1:
        # phone.append(h.text)
        print(h.text)      

driver.quit()



