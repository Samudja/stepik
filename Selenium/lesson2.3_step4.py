from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    option1 = browser.find_element_by_tag_name("button").click()
    option2 = browser.switch_to.alert
    option2.accept()
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)
    
    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(y)
    
    option3 = browser.find_element_by_tag_name("button").click()
    
finally:
    time.sleep(15)
    browser.quit()    