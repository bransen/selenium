from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get ("https://qaweb2.cps.golf/BWDWebstore/")

print(driver.title)

search = driver.find_element(By.ID, "s")
search.send_keys("test")
search.send_keys(Keys.RETURN)


time.sleep(5)

driver.quit()