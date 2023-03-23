from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

chromedriver_autoinstaller.install()
link = "https://suninjuly.github.io/selects2.html"

def sum(x, y):
    return str(int(x) + int(y))

try:

    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text
    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text
    z = str(sum(x, y))
    browser.find_element(By.ID, "dropdown").click()
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(value=str(z))
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
# не забываем оставить пустую строку в конце файла