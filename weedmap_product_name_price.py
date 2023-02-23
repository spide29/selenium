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
driver.get('https://weedmaps.com/dispensaries/harmony-dispensary')

conn = sqlite3.connect('dispensary_data.db')

conn.execute('''CREATE TABLE IF NOT EXISTS dispensary_data
             (name TEXT, price TEXT)''')
list = []
list1=[]
list2=[]
visited=[]
h1_list = []
price_list = []
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
            h1_list.append(h.text)
        price = driver.find_elements(By.CLASS_NAME,"jiFdiN")
        for p in price:
             price_list.append(p.text)
             
        for h, p in zip(h1_list, price_list):
            conn.execute("INSERT INTO dispensary_data (name, price) VALUES (?, ?)", (h, p))

        conn.commit()
conn.close()


        

driver.quit()







# df = pd.DataFrame({'text': visited})
# # df.to_excel('output29.xlsx', index=False)
# data = {"Title": h1_list, "Price": price_list}
# df = pd.DataFrame(data)
# with pd.ExcelWriter("data.xlsx") as writer:
#     df.to_excel(writer, index=False)