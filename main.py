from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://passport.yandex.ru/auth/')
name = driver.find_element('id', 'passp-field-login')
name.send_keys('reanim86')
name_click = driver.find_element('id', 'passp:sign-in')
name_click.click()
wait.until(visibilityOfElementLocated(By.id("menu")))
password = driver.find_element('id', 'passp-field-passwd')
# password.send_keys('Tehn4321')
