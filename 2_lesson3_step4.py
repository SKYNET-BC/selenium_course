from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector('button.btn.btn-primary').click()

    browser.switch_to.alert.accept()

    time.sleep(1)

    y = calc(browser.find_element_by_css_selector('span#input_value').text)

    browser.find_element_by_id('answer').send_keys(y)

    browser.find_element_by_css_selector('button.btn.btn-primary').click()


except Exception as error:
    print(f'Произошла ошибка: {error}')


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    print(browser.switch_to.alert.text)
    # закрываем браузер после всех манипуляций
    browser.quit()
