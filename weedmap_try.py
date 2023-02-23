import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, executable_path="F:\\1.2 MIT Django Project\\chromedriver.exe")
driver.get('https://weedmaps.com/dispensaries/harmony-dispensary')


list = []
list1 =[]
visited=[]
content_blocks = driver.find_elements(By.CLASS_NAME,"cvibnt")


for block in content_blocks:
    elements = block.find_elements(By.TAG_NAME,"a")
    for el in elements:
        list.append(el.get_attribute("href"))
        print(list)
for link in list:
    driver.get(link)
    blocks = driver.find_elements(By.CLASS_NAME,"lloEgg")

    for block in blocks:
        element = block.find_elements(By.TAG_NAME,"a")
        for el in element:
            
            list1.append(el.get_attribute("href"))
            print(list1)
    for links in list1:
        driver.get(links)
    list1 = []
    driver.back()

driver.quit()




















# df = pd.DataFrame({'text': links})
# # df.to_excel('output.xlsx', index=False)
    

# # link_element = driver.find_element(By.XPATH , '//*[@id="content"]/div[3]/div/div[1]/a')
# # link_element.click()

# link_els = driver.find_elements(By.CLASS_NAME, 'cvibnt')
# link_elss = link_els.find_elements(By.TAG_NAME,"a")


# links = []
# for link_el in link_elss:
#     href = link_el.get_attribute('href')
#     links.append(href)
#     print(links)