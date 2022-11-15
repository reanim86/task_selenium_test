from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login_ya(ya_login, ya_password):
    """
    Функция логинится на странице yandex.ru
    :param ya_login: login on yandex
    :param ya_password: password
    :return:
    """
    driver = webdriver.Chrome()
    driver.get('https://passport.yandex.ru/auth/')
    email = driver.find_element(By.CLASS_NAME, 'AuthLoginInputToggle-type')
    email.click()
    name = driver.find_element('id', 'passp-field-login')
    name.send_keys(ya_login)
    name_click = driver.find_element('id', 'passp:sign-in')
    name_click.click()
    time.sleep(0.4)
    password = driver.find_element('id', 'passp-field-passwd')
    password.send_keys(ya_password)
    pass_click = driver.find_element('id', 'passp:sign-in')
    pass_click.click()
    time.sleep(1)
    return driver.title
