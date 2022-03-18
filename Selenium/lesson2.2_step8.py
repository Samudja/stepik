from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    option1 = browser.find_element_by_name("firstname")
    option1.send_keys("Pypa")
    option2 = browser.find_element_by_name("lastname")
    option2.send_keys("Lypa")
    option3 = browser.find_element_by_name("email")
    option3.send_keys("123@mail.ru")
    option4 = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt') 
    option4.send_keys(file_path)
    option5 = browser.find_element_by_tag_name("button").click()
    
finally:
    time.sleep(15)
    browser.quit()