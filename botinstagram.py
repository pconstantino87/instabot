import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(
            executable_path=r"/Users/masterpe/Documents/dev/geckodriver/geckodriver")

# name="username" name="password"
    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(2)
        #login_button = driver.find_element_by_xpath("//a[@href=auth_switcher]")
        # login_button.click()

        user_element = driver.find_element(By.XPATH,
                                           "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)

        pass_element = driver.find_element(By.XPATH,
                                           "//input[@name='password']")
        pass_element.clear()
        pass_element.send_keys(self.password)
        pass_element.send_keys(Keys.RETURN)
        time.sleep(5)

    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(5)
        for i in range(1, 4):
            driver.execute_script(
                "window.scroll(0, document.body.scroolHeigth);")


print('Usuario')
u = input()
print('senha')
s = input()
print('hastag')
h = input()

mpigbot = InstagramBot(u, s)
mpigbot.curtir_fotos(h)
