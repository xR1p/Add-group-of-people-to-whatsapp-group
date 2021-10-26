import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def group_add(name):
    gr=[]
    with open('Samples/people.csv','rt')as f:
      data = csv.reader(f)
      for row in data:
          if row[1] != "Write a Name":
            gr.append(row[1])
    driver = webdriver.Firefox()
    driver.maximize_window()
    r=driver.get('https://web.whatsapp.com/')
    time.sleep(20)
    try:
        driver.find_element_by_xpath('//*[@title="{}"]'.format(name)).click()
    except:
        print("group doesn't exist")
        print("Try again")
        return
    f = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//*[@class="_3V5x5"]')))
    f.click()
    f = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//*[@class="_3p0T6"]')))
    f.click()
    """
    driver.find_elements_by_class_name("_3V5x5")[0].click()
    time.sleep(25)
    driver.find_elements_by_class_name("_3p0T6")[0].click()
    """
    for i in gr :
        driver.find_element_by_xpath('//*[@title="Search…"]').send_keys(i)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@title="{}"]'.format(i)).click()

    driver.find_element_by_xpath('//*[@data-icon="checkmark-light"]').click()
    time.sleep(5)
    f = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//*[@class="_2eK7W _3PQ7V"]')))
    f.click()
    return

name=input("Enter the name of the group that you want add people to ")
group_add(name)