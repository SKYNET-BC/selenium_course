from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('span#input_value')
    x = x_element.text
    y = calc(x)

    browser.find_element_by_id('answer').send_keys(y)

    browser.find_element_by_id('robotCheckbox').click()

    browser.execute_script('window.scrollBy(0, 150);')

    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector('button.btn.btn-primary').click()

    time.sleep(1)


except Exception as error:
    print(f'Произошла ошибка: {error}')


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
