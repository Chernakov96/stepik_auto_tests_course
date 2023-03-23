from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    #input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first") # работает!
    input1 = browser.find_element(By.CSS_SELECTOR, "input.first:required")
    input1.send_keys("Anastasia")
    #input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    input2 = browser.find_element(By.CSS_SELECTOR, "input.second:required")
    input2.send_keys("Propuskova")
    #input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    input3 = browser.find_element(By.CSS_SELECTOR, "input.third:required")
    input3.send_keys("abegorskaya@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    