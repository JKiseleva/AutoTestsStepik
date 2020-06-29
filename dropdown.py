from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
    return str(input1+input2)

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_css_selector("#num1")
    a = input1.text
    input2 = browser.find_element_by_css_selector("#num2")
    b = input2.text
    y = int(a) + int(b)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(y))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла