import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import pandas as pd
from selenium.common.exceptions import NoSuchElementException


options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, executable_path="F:\\Selenium\\chromedriver.exe")
driver.get('https://weedmaps.com/dispensaries/in/united-states')

state = []
city=[]
disp=[]
list = []
list1=[]
list2=[]
visited=[]
loc=[]
vvisited=[]
temp=[]
links = []



div = driver.find_elements(By.CLASS_NAME, 'eODPbn')
for d in div:
    link_els = d.find_elements(By.CLASS_NAME, 'kmzmTS')
    for link_el in link_els:
        href = link_el.get_attribute('href')
        state.append(href)

for link in state:
    driver.get(link)
    div = driver.find_elements(By.CLASS_NAME, 'eODPbn')
    for d in div:
        link_els = d.find_elements(By.CLASS_NAME, 'kmzmTS')
        for link_el in link_els:
            href = link_el.get_attribute('href')
            city.append(href)

    for link in city:
        driver.get(link)
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
            
            h1 = driver.find_elements(By.XPATH,'//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[5]')
            for h in h1:
                # purchesh.append(h.text)
                print(h.text)

            h1 = driver.find_elements(By.XPATH,'//*[@id="content"]/div[3]/div[1]/div[1]/div[2]/div[4]/div/div[3]/a[1]/div[2]')
            for h in h1:
                # phone.append(h.text)
                print(h.text)  
        # div = driver.find_elements(By.CLASS_NAME, 'fBAocb')
        # for d in div:
        #     link_els = d.find_elements(By.CLASS_NAME, 'ApPmp')
        #     for link_el in link_els:
        #         href = link_el.get_attribute('href')
        #         loc.append(href)
        # for link in loc:
        #     driver.get(link)
        #     h1 = driver.find_elements(By.XPATH,'//*[@id="sb_ifc51"]/input')
        #     for h in h1:
        #         print(h.text)
        
            content_blocks = driver.find_elements(By.CLASS_NAME,"cvibnt")       
            for block in content_blocks:
                elements = block.find_elements(By.TAG_NAME,"a")
                for el in elements:
                    list.append(el.get_attribute("href"))
            for link in list:
                driver.get(link)
                while True:

                    blocks = driver.find_elements(By.CLASS_NAME,"lloEgg")
                    for block in blocks:
                        element = block.find_elements(By.TAG_NAME,"a")
                        for el in element:
                            list1.append(el.get_attribute("href"))

                        
                    blocksss = driver.find_elements(By.CLASS_NAME,'kmGAHV')
                    for blockss in blocksss:
                        block = blockss.find_elements(By.CLASS_NAME,'cVQPKf')
                    for href in block:
                        list2.append(href.get_attribute("href"))
                    
                    if list2[1] is None:
                        list2=[]
                        visited.extend(list1)
                        list1=[]
                        break

                    else:
                        driver.get(list2[1])
                        list2=[]
                        visited.extend(list1)
                        list1=[]
                for links in visited:
                    driver.get(links)
                    h1 = driver.find_elements(By.TAG_NAME,"h1")
                    for h in h1:
                        print(h.text)
                    price = driver.find_elements(By.CLASS_NAME,"jiFdiN")
                    for p in price:
                        print(p.text)

driver.quit()





# df = pd.DataFrame({'text': disp})
# df.to_excel('desp.xlsx', index=False)