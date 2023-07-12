from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


#from selenium.webdriver.chrome.options import Options as ChromeOptions


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demoblaze.com")
login= driver.find_element(By.ID,"login2")
login.click()

time.sleep(2)

driver.find_element(By.ID,"loginusername").send_keys("ADMIN")
driver.find_element(By.ID,"loginpassword").send_keys("ADMIN")

time.sleep(2)


driver.find_element(By.XPATH, "//button[@onclick='logIn()']").click()


time.sleep(2)

element = driver.find_element(By.XPATH, "//a[@id='nava']").text
# search_text = "PRODUCT STORE"
# if search_text in element.text:
#     print(f"The element contains the {search_text}.")
# else:
#     print(f"The element does not contain the search text: {search_text}.")
assert element =="PRODUCT STORE"

time.sleep(2)

driver.find_element(By.ID,"logout2").click()
time.sleep(3)


driver.close()
driver.quit()