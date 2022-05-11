from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_img = browser.find_element_by_id('treasure')
    x_val = x_img.get_attribute('valuex')
    x = int(x_val)
    y = calc(x)

    txt_fld = browser.find_element_by_id('answer')
    txt_fld.send_keys(y)

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    r_button = browser.find_element_by_id('robotsRule')
    r_button.click()

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
