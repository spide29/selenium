from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome( executable_path="F:\\Selenium\\chromedriver.exe")


# driver.get("https://www.cnil.fr/en/actualite")
# print(driver.title)
# print(driver.current_url) 



# driver.get("https://webmail.au.syrahost.com/")
driver.get("https://www.tutorialspoint.com/market/login.jsp")
driver.maximize_window()





email_field = driver.find_element("id","user_email")
email_field.send_keys("swapnilkansara29@gmail.com")
time.sleep(5)
password_field = driver.find_element("id", "user_password")
password_field.send_keys("swapnilsujal29")
time.sleep(5)
submit_button = driver.find_element(By.XPATH , ".//button[@type='submit']")
submit_button.click()
time.sleep(10)
driver.implicitly_wait(10)
driver.get("https://www.tutorialspoint.com/market/student/dashboard.jsp?v=1675677598")



driver.quit()
