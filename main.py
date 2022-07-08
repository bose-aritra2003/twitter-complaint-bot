import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.<NAME OF BROWSER>.service import Service

WEB_DRIVER_PATH = <PATH TO YOUR DESIRED WEB DRIVER>

SPEED_TEST_URL = 'https://www.speedtest.net/'
TWITTER_URL = 'https://twitter.com/'

PROMISED_DOWN = float(input("Enter your the download speed promised to you: "))
PROMISED_UP = float(input("Enter your the upload speed promised to you: "))
TWITTER_EMAIL = input("Enter your email: ")
TWITTER_PASSWORD = input("Enter your password: ")


class InternetSpeedTwitterBot:
    def __init__(self):
        # Initialising web driver
        self.web_driver_service = Service(executable_path=WEB_DRIVER_PATH)
        self.driver = webdriver.<NAME OF BROWSER>(service=self.web_driver_service)
        self.driver.maximize_window()

        # Properties
        self.down = 0.0
        self.up = 0.0

    def getInternetSpeed(self):
        self.driver.get(SPEED_TEST_URL)
        go_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]'
        go_button = self.driver.find_element(By.XPATH, go_xpath)
        go_button.click()

        # Wait for speeds to show up to load
        while True:
            try:
                down_speed_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'
                down_speed = self.driver.find_element(By.XPATH, down_speed_xpath).get_attribute("textContent")
                self.down = float(down_speed)

                up_speed_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
                up_speed = self.driver.find_element(By.XPATH, up_speed_xpath).get_attribute("textContent")
                self.up = float(up_speed)
            except NoSuchElementException:
                time.sleep(2)
            except ValueError:
                time.sleep(2)
            else:
                break

        print(self.down)
        print(self.up)

    def tweetAtProvider(self):
        self.driver.get(TWITTER_URL)
        while True:
            try:
                sign_in_button_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span'
                sign_in_button = self.driver.find_element(By.XPATH, sign_in_button_xpath)
                sign_in_button.click()
            except NoSuchElementException:
                time.sleep(2)
            else:
                break

        while True:
            try:
                email_field_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
                email_field = self.driver.find_element(By.XPATH, email_field_xpath)
                email_field.send_keys(TWITTER_EMAIL)

                next_button_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span'
                next_button = self.driver.find_element(By.XPATH, next_button_xpath)
                next_button.click()
            except NoSuchElementException:
                time.sleep(2)
            else:
                break

        while True:
            try:
                password_field_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
                password_field = self.driver.find_element(By.XPATH, password_field_xpath)
                password_field.send_keys(TWITTER_PASSWORD)

                login_button_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span'
                login_button = self.driver.find_element(By.XPATH, login_button_xpath)
                login_button.click()
            except NoSuchElementException:
                time.sleep(2)
            else:
                break

        while True:
            try:
                whats_happening_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
                whats_happening = self.driver.find_element(By.XPATH, whats_happening_xpath)
                whats_happening.click()
                whats_happening.send_keys(f'Hey Internet Service Provider. I was promised a speed of {PROMISED_DOWN} Mbps download and {PROMISED_UP} Mbps upload. But I am getting {self.down} Mbps download and {self.up} Mbps upload. Please fix this issue!')
                tweet_button_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span'
                tweet_button = self.driver.find_element(By.XPATH, tweet_button_xpath)
                tweet_button.click()
            except NoSuchElementException:
                time.sleep(2)
            else:
                break


bot = InternetSpeedTwitterBot()
bot.getInternetSpeed()
if bot.down < (PROMISED_DOWN - 10) or bot.up < (PROMISED_UP - 10):
    bot.tweetAtProvider()
bot.driver.quit()


