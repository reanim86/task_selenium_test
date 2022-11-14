from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://passport.yandex.ru/auth/')
name = driver.find_element('id', 'passp-field-login')
name.send_keys('reanim86')