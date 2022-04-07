# To automate job application process on linkedin
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from twitter_credentials import *
import time
PROMISED_DOWN = 50
PROMISED_UP = 50
timeout = time.time() + 60*4
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
s = Service("A:\Webservices ML\chromedriver (2).exe")
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.maximize_window()
# Testing speed of the  network connection
driver.get("https://fast.com/")
# driver.find_element(by=By.CLASS_NAME, value="start-text").click()
element_found = False
time.sleep(10)
while not element_found:
    try:
        driver.find_element(by=By.ID, value='show-more-details-link').click()
        element_found = True
        time.sleep(10)
    except:
        time.sleep(5)
        print("Element not found")
        continue

down_speed = int(driver.find_element(by=By.ID, value='speed-value').text)
print(down_speed)
element_found = False
while not element_found:
    try:
        driver.find_element(by=By.ID, value='upload-value')
        element_found = True
    except NoSuchElementException:
        time.sleep(5)
        print("Element upload not found")
        continue

upload_speed = int(driver.find_element(by=By.ID, value='upload-value').text)
print(upload_speed)
if upload_speed < PROMISED_UP or down_speed < PROMISED_DOWN:
    print("Network is not good")
    driver.get("https://twitter.com/i/flow/login")
    element_found = False
    while not element_found:
        try:
            dd = driver.find_element(by=By.NAME, value="text")
            dd.send_keys(username)
            dd.send_keys(Keys.ENTER)
            element_found = True
            time.sleep(5)
        except NoSuchElementException:
            time.sleep(5)
            print("Element upload not found")
            continue

    element_found = False
    while not element_found:
        try:
            dd = driver.find_element(by=By.NAME, value='password')
            dd.send_keys(password)
            dd.send_keys(Keys.ENTER)
            element_found = True
        except NoSuchElementException:
            time.sleep(5)
            print("Element upload not found")
            continue
        time.sleep(5)
        tweet_compose = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/'
                                                     'div[2]/div/div[2]/div[1]/'
                                                     'div/div/div/div[2]/div[1]/div/div/div/div/div/'
                                                     'div/div/div/div/'
                                                     'label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {down_speed}down/" \
                f"{upload_speed}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = driver.find_element(By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/'
            'div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
        tweet_button.click()
        time.sleep(2)
        driver.quit()



