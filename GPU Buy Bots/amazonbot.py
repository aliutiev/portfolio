from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains


import time
import sys
import random

options = Options()
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-browser-side-navigation")
options.add_argument("--disable-gpu")

# instance of the WebDriver
driver = webdriver.Chrome('C:/Users/Andrew/Documents/Projects/chromedriver.exe', chrome_options=options)
action = ActionChains(driver)

username = ""
password = ""

page_url = "https://www.amazon.ca/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.ca%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=caflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"
driver.get(page_url)

# username input
user = driver.find_elements_by_xpath("//*[@id='ap_email']")
user[0].send_keys(username)

# login button
form_submit = driver.find_elements_by_xpath("//*[@id='continue']")
form_submit[0].click()

# password input
user = driver.find_elements_by_xpath("//*[@id='ap_password']")
user[0].send_keys(password)

# login button
form_submit = driver.find_elements_by_xpath("//*[@id='signInSubmit']")
form_submit[0].click()



page_urls = [   
                # 3080 - Asus OC, MSI Gaming, Asus ROG Strix
                "https://www.amazon.ca/dp/B08HH5WF97/#aod",
                "https://www.amazon.ca/dp/B08HR7SV3M/#aod",
                "https://www.amazon.ca/dp/B08J6F174Z/#aod",

                # 3070 - ASUS Ko, Asus Dual
                "https://www.amazon.ca/dp/B08MT6B58K/#aod",
                "https://www.amazon.ca/dp/B08L8LG4M3/#aod",

                # 3060ti - Asus 3060 ti OC
                "https://www.amazon.ca/dp/B08P2HBBLX/#aod",

                ]

# random index for multiple instances
length = len(page_urls) 
index = random.randint(0, length - 1)

driver.get(page_urls[index])

def enable_oneclick():

    print("One-click enabled")
   
    page_url = "https://www.amazon.ca/cpe/yourpayments/settings/manageoneclick?ref_=v1c_title"
    driver.get(page_url)

    click_action = driver.find_elements_by_xpath("//*[@class='a-switch-control']")
    click_action[0].click()    

def buy_now(): 
    print("Attempting to purchase")

    click_action = driver.find_elements_by_xpath("//*[@id='placeYourOrder']/span/input")
    click_action[0].click()

    time.sleep(5)

enable_oneclick()

while True:
    
    print("Checking")
    # checkout buttons then buy
    if bool(driver.find_elements_by_xpath("//*[@id='turbo-checkout-pyo-button']")) == True:
        click_action = driver.find_elements_by_xpath("//*[@id='turbo-checkout-pyo-button']")
        click_action[0].click()

        buy_now()

    elif bool(driver.find_elements_by_xpath("//*[@id='buy-now-button']")) == True:
        click_action = driver.find_elements_by_xpath("//*[@id='buy-now-button']")
        click_action[0].click()

        buy_now()

    else:
        time.sleep(3)
        driver.get(page_urls[index % length])
        index += 1
        

