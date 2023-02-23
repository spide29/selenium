# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd
# from selenium.common.exceptions import NoSuchElementException
# import sqlite3

# options = webdriver.ChromeOptions() 
# options.add_argument("start-maximized")
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options, executable_path="F:\\1.2 MIT Django Project\\chromedriver.exe")
# driver.get('https://weedmaps.com/dispensaries/harmony-dispensary')

# conn = sqlite3.connect('dispensary_data.db')

# conn.execute('''CREATE TABLE dispensary_data
#              (name TEXT, price TEXT)''')
# list = []
# list1=[]
# list2=[]
# visited=[]
# h1_list = []
# price_list = []
# content_blocks = driver.find_elements(By.CLASS_NAME,"cvibnt")

# for block in content_blocks:
#     elements = block.find_elements(By.TAG_NAME,"a")
#     for el in elements:
#         list.append(el.get_attribute("href"))
# for link in list:
#     driver.get(link)
#     while True:

#         blocks = driver.find_elements(By.CLASS_NAME,"lloEgg")
#         for block in blocks:
#             element = block.find_elements(By.TAG_NAME,"a")
#             for el in element:
#                 list1.append(el.get_attribute("href"))

              
#         blocksss = driver.find_elements(By.CLASS_NAME,'kmGAHV')
#         for blockss in blocksss:
#             block = blockss.find_elements(By.CLASS_NAME,'cVQPKf')
#         for href in block:
#             list2.append(href.get_attribute("href"))
          
#         if list2[1] is None:
#             list2=[]
#             visited.extend(list1)
#             list1=[]
#             break

#         else:
#             driver.get(list2[1])
#             list2=[]
#             visited.extend(list1)
#             list1=[]
#     for links in visited:
#         driver.get(links)
#         h1 = driver.find_elements(By.TAG_NAME,"h1")
#         for h in h1:
#             h1_list.append(h.text)
#         price = driver.find_elements(By.CLASS_NAME,"jiFdiN")
#         for p in price:
#              price_list.append(p.text)

# for h, p in zip(h1_list, price_list):
#     conn.execute("INSERT INTO dispensary_data (name, price) VALUES (?, ?)", (h, p))

# conn.commit()
# conn.close()


# driver.quit()


       
# df = pd.DataFrame({'text': visSited})
# df.to_excel('output29.xlsx', index=False)






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
list1=[]
list2=[]
visited=[]
h1_list = []
price_list = []

while True:

    div = driver.find_elements(By.CLASS_NAME, 'eQOCGV')
    for d in div:
        link_els = d.find_elements(By.TAG_NAME, 'a')
        for link_el in link_els:
            href = link_el.get_attribute('href')
            list1.append(href)
            
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
    
             



        

driver.quit()



