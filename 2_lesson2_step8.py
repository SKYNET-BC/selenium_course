from selenium import webdriver
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector('input[name="firstname"]').send_keys('Name')
    browser.find_element_by_css_selector('input[name="lastname"]').send_keys('Last')
    browser.find_element_by_css_selector('input[name="email"]').send_keys('Mail')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file_2_les2_s8.txt')
    browser.find_element_by_id('file').send_keys(file_path)

    browser.find_element_by_css_selector('button.btn.btn-primary').click()

    time.sleep(1)


except Exception as error:
    print(f'Произошла ошибка: {error}')


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
