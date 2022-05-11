from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")


try:
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
        )
    browser.find_element_by_id('book').click()
    time.sleep(1)

    y = calc(browser.find_element_by_id('input_value').text)

    browser.find_element_by_id('answer').send_keys(y)

    browser.find_element_by_id('solve').click()

    print(browser.switch_to.alert.text)

    # assert "successful" in message.text

except Exception as error:
    print(f'Произошла ошибка: {error}')


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)

    # закрываем браузер после всех манипуляций
    browser.quit()
