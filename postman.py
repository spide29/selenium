import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="F:\\Selenium\\chromedriver.exe")


driver.get("https://identity.getpostman.com/login")


email_field = driver.find_element("id","username")
email_field.send_keys("swapnilkansara29@gmail.com")

password_field = driver.find_element("id", "password")
password_field.send_keys("swapnilsujal29")

submit_button = driver.find_element(By.XPATH , '//*[@id="sign-in-btn"]')
submit_button.click()
time.sleep(5)
driver.get("https://web.postman.co/workspace/My-Workspace~75fbd85d-ded0-408d-8517-c110d14e2d3c/request/create?requestId=5eca83f4-78a5-4f39-b089-941aa9f7e818")
time.sleep(5)
driver.find_element(By.CLASS_NAME, 'IconWrapper__IconContainer-gnjn48-0 gkhcSN dropdown-caret').click()
time.sleep(5)
driver.quit()
