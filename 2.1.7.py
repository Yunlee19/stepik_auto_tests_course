import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# Инициализация браузера
browser = webdriver.Chrome()
try:
    # Открываем страницу
    browser.get("http://suninjuly.github.io/get_attribute.html")
    
    # Находим элемент-картинку и берем значение атрибута valuex
    treasure_img = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x_value = treasure_img.get_attribute("valuex")
    
    # Вычисляем математическую функцию
    y = calc(x_value)
    
    # Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(y)
    
    # Отмечаем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()
    
    # Выбираем radiobutton "Robots rule!"
    robots_rule_radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robots_rule_radio.click()
    
    # Нажимаем на кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    
    
finally:
    # Даем время для загрузки результата
    time.sleep(10)
    # Закрываем браузер
    browser.quit()
