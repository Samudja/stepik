from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    findx = browser.find_element_by_id("treasure")
    havex = findx.get_attribute("valuex")
    print("x =", havex)
    assert havex is not None
    
    x = havex
    y = calc(x)
    
    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(y)
    
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    option3 = browser.find_element_by_xpath("//button[@type='submit']")
    option3.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла