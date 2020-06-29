from selenium import webdriver
import time
import math

def calc(sunduk_value):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

#значение атрибута
    
    x_element = browser.find_element_by_id("treasure")
    sunduk_value = x_element.get_attribute("valuex")
    x = sunduk_value
    y = calc(x)
    
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    
    input2 = browser.find_element_by_css_selector("#robotCheckbox")
    input2.click()
    
    input3 = browser.find_element_by_css_selector("#robotsRule")
    input3.click()
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


import time
import math
from selenium import webdriver


LINK = 'http://suninjuly.github.io/get_attribute.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome(executable_path='./chromedriver')
    browser.get(LINK)
    treasure_img = browser.find_element_by_css_selector('#treasure')
    value_x = treasure_img.get_attribute('valuex')
    x = calc(int(value_x))
    browser.find_element_by_css_selector('#answer').send_keys(x)
    browser.find_element_by_css_selector('#robotCheckbox').click()
    browser.find_element_by_css_selector('#robotsRule').click()
    browser.find_element_by_css_selector('button[type="submit"]').submit()

finally:
    time.sleep(10)
    browser.quit()