from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


def calc(x, y):
  return x + y


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text

    total = calc(int(num1), int(num2))

    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(str(total))

    button = browser.find_element_by_css_selector('button.btn.btn-default')
    button.click()

    time.sleep(1)


except Exception as error:
    print(f'Произошла ошибка: {error}')


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
