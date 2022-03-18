import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    number1 = browser.find_element_by_id("num1")
    number2 = browser.find_element_by_id("num2")
    number1_value = int(number1.text)
    number2_value = int(number2.text)
    print("Первое значение:", number1_value)
    print("Второе значение:", number2_value)
    
    total_value = int(number1_value) + int(number2_value)
    print("Нужный нам ответ:", total_value)
    
    summ = Select(browser.find_element_by_id("dropdown"))
    summ.select_by_visible_text(str(total_value))
    print("Выбираем значение в селекте сайта, в данном случае", total_value)
    
    browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(30)
    browser.quit()

    
    
