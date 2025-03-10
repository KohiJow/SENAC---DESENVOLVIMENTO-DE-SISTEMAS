from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_login_instagram():
    driver = webdriver.Edge()
    driver.get('https://www.instagram.com/accounts/login/')

    time.sleep(2)
    user_input = driver.find_element(By.NAME, "username")
    pass_input= driver.find_element(By.NAME, 'password')

    user_input.send_keys('seu_usuario')
    pass_input.send_keys('sua_senha')

    pass_input.send_keys(Keys.RETURN)

    time.sleep(5)

    assert 'Instagram' in driver.title

    driver.quit()

test_login_instagram()
