import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


# driver_path= ('F:\\1.2 MIT Django Project\\chromedriver.exe')
# driver = webdriver.Chrome(executable_path= driver_path)
# url = "https://www.amazon.in/"
# driver.get(url)
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
# to supress the error messages/logs
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, executable_path="F:\\Selenium\\chromedriver.exe")
driver.get('https://www.amazon.in/')


link_element = driver.find_element(By.XPATH , '//*[@id="nav-hamburger-menu"]/span')
link_element.click()

link_els = driver.find_elements(By.XPATH, '//*[@id="hmenu-content"]/ul[1]/li/a')
links = []
for link_el in link_els:
    href = link_el.get_attribute('href')
    links.append(href)
    visited_links = []
    for link in links:
        if link not in visited_links:
            driver.get(link)
            visited_links.append(link)
            link_elss = driver.find_elements(By.CLASS_NAME, 'a-link-normal')
            linksm = []
            for link_els in link_elss:
                href = link_els.get_attribute('href')
                linksm.append(href)
            for linkm in linksm:
                if linkm not in visited_links:
                    driver.get(linkm)
                    visited_links.append(linkm)
                    driver.back()
            driver.back()

        


        



df = pd.DataFrame({'text': linksm})
df.to_excel('output2.xlsx', index=False)

driver.quit()
