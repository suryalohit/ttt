

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
  chrome_options = Options()
  chrome_options.add_argument("--headless")

  driver = webdriver.Chrome(options=chrome_options)






  driver.get('https://x.com/i/flow/login/')
  time.sleep(3)
  username = driver.find_element("name", "text")
  username.click()
  print("1")
  username.send_keys('retiredHippo')
  print('retiredhippo')
  next=driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
  next.click()
  time.sleep(3)
  try:
    phhh = driver.find_element("name", "text")
    print("21")
    phhh.click()
    print("22")
    phhh.send_keys('91003388289')
    print("23")
    ph=driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button')
    print("24")
    ph.click()
    print("25")
    time.sleep(3)
  except:
    print("An exception occurred")
    print("255")
  print("2")


  password = driver.find_element("name", "password")
  password.click()
  password.send_keys('Asailohit30@')


  signin=driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
  signin.click()

  print("3")

  time.sleep(3)
  driver.get('https://x.com/DaoKwonDo/')
  time.sleep(4)
  prof=driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/a')
  print(prof.get_attribute("href"))
  print("all okk")  


if __name__ == "__main__":
  main()

