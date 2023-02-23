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
    counter = 0
    while counter < len(links):
        for j in range(len(links)):
            driver.get(links[j])
            link_elss = driver.find_elements(By.CLASS_NAME, 'a-size-base a-inline-block')
            linksm = []
            for link_els in link_elss:
                href = link_els.get_attribute('href')
                linksm.append(href)
                for i in range(len(links)):
                    driver.get(linksm[i])
                    i = i + 1
                    driver.back()
                driver.back()
        link_element = driver.find_element(By.XPATH , '//*[@id="nav-hamburger-menu"]/span')
        link_element.click()        
        counter = counter + 1

driver.quit()
