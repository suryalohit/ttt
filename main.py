

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options




print("Prepare start")
def main():

  print("Prepare start")
  time.sleep(6)
  chrome_options = Options()
  chrome_options.add_argument("--headless")

  driver = webdriver.Chrome(options=chrome_options)





  driver.get('https://www.cricbuzz.com/')
  time.sleep(3)
  next=driver.find_element("xpath", '//*[@id="cb-main-menu"]/a[2]')
  print(next.text)
  time.sleep(5)
  

  
if __name__ == "__main__":
  main()

