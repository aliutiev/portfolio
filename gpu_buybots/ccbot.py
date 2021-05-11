from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

import time
import sys
import random

# instance of the WebDriver
driver = webdriver.Chrome('C:/Projects/chromedriver.exe')
action = ActionChains(driver)

username = ""
password = ""
credit_card = ""
last_name = ""

# navigate to cc & accept cookies   
page_url = "https://www.canadacomputers.com"
driver.get(page_url)
click_action = driver.find_elements_by_xpath("//*[@id='privacy-btn']")
click_action[0].click()

# login button to cc
form_submit = driver.find_elements_by_xpath("//*[@id='header-search']/div/div[3]/div/div[1]/a")
form_submit[0].click()

# username input
user = driver.find_elements_by_xpath("//*[@id='lo-username']")
user[0].send_keys(username)

# password & submit to cc
pw = driver.find_elements_by_xpath("//*[@id='lo-password']")
pw[0].send_keys(password)

# login submit to cc
form_submit = driver.find_elements_by_xpath("//*[@id='btn-login']")
form_submit[0].click()

passed_captcha = input("Did you pass the captcha? y/n")

if passed_captcha != "y":
    sys.exit()
                

page_urls = [   

                # "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=186197", 
                # "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=186310",
                # "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183637", 
                # "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183210", 
                # "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=184168",
                # "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183638",
                # "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183498",
                # "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=187683",
                # "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183209",
                # "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183636",
                # "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=185675",
                # "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183100",
                # "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183499",
                # "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183208",
                # "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183561",
                # "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183560",                
                # "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=181353",
                # "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=182755",
                # "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183210",
                # "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=181415",

                "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=184167",
                "https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=183638"


                
            
                ]

# random index for multiple instances
length = len(page_urls) 
index = random.randint(0, length - 1)

driver.get(page_urls[index])


def go_to_checkout(): 
    print("Attempting to go to checkout")


    # add to cart
    click_action = driver.find_elements_by_xpath("//*[@id='btn-addCart'][1]")
    click_action[0].click()

    # checkout
    click_action = driver.find_elements_by_xpath("//*[@id='btn-checkout']")
    click_action[0].click()

    

    delivery()

def delivery():
    print("Delivery Selection")

    # pickup in store
    click_action = driver.find_elements_by_xpath("//*[contains(text(), 'Reserve & pick-up at store')]")
    click_action[0].click()

    # select waterloo or otherstores
    if bool(driver.find_elements_by_xpath("//*[@id='WATERLOO']")):
        click_action = driver.find_elements_by_xpath("//*[@id='WATERLOO']")
        click_action[0].click()
    elif bool(driver.find_elements_by_xpath("//*[@id='CA']")):
        click_action = driver.find_elements_by_xpath("//*[@id='CA']")
        click_action[0].click()
    elif bool(driver.find_elements_by_xpath("//*[@id='MISS']")):
        click_action = driver.find_elements_by_xpath("//*[@id='MISS']")
        click_action[0].click()
    elif bool(driver.find_elements_by_xpath("//*[@id='ETOB']")):
        click_action = driver.find_elements_by_xpath("//*[@id='ETOB']")
        click_action[0].click()
    elif bool(driver.find_elements_by_xpath("//*[@id='OA']")):
        click_action = driver.find_elements_by_xpath("//*[@id='OA']")
        click_action[0].click()
    elif bool(driver.find_elements_by_xpath("//*[@id='BURL']")):
        click_action = driver.find_elements_by_xpath("//*[@id='BURL']")
        click_action[0].click()
    elif bool(driver.find_elements_by_xpath("//*[@id='HAM2']")):
        click_action = driver.find_elements_by_xpath("//*[@id='HAM2']")
        click_action[0].click()
    else:
        reset()
        return
    
    # next page
    click_action = driver.find_elements_by_xpath("//*[@id='ch-form']/div[2]/div/button[2]")
    click_action[0].click()

    

    payment()

    

def payment():
    print("Money")

    if bool(driver.find_elements_by_xpath("//*[@id='check-out']/div[2]/form/div[2]/div/button[2]")):
        click_action = driver.find_elements_by_xpath("//*[@id='check-out']/div[2]/form/div[2]/div/button[2]")
        click_action[0].click()

    # master card confirmation
    if bool(driver.find_elements_by_xpath("//*[@id='ch-frm-paymentcontact-card-number']")):
        credit_card = driver.find_elements_by_xpath("//*[@id='ch-frm-paymentcontact-card-number']")
        credit_card[0].send_keys(password)

    # last name confirmation
    if bool(driver.find_elements_by_xpath("//*[@id='ch-frm-paymentcontact-card-holder']")):
        last_name = driver.find_elements_by_xpath("//*[@id='ch-frm-paymentcontact-card-holder']")
        last_name[0].send_keys(password)


    # submit to review
    if bool(driver.find_elements_by_xpath("//*[@id='check-out']/div[2]/form/div[2]/div/button[2]")):
        click_action = driver.find_elements_by_xpath("//*[@id='check-out']/div[2]/form/div[2]/div/button[2]")
        click_action[0].click()

    purchase()

def purchase():
    print("Attempting to purchase")

    # place order
    click_action = driver.find_elements_by_xpath("//*[@id='check-out']/div[2]/form/div[3]/div/button[2]")
    click_action[0].click()

    print("Purchased")


    time.sleep(20)


def reset():
    # emptying the cart to keep going forward
    driver.get("https://www.canadacomputers.com/shopping_cart.php")
    if bool(driver.find_elements_by_xpath("//*[@id='shopping_cart']/div[2]/div/div[2]/div/div[2]/p/i")):
        click_action = driver.find_elements_by_xpath("//*[@id='shopping_cart']/div[2]/div/div[2]/div/div[2]/p/i")
        click_action[0].click()
    
    time.sleep(30)

while True:
    
    # check to see if we're still signed in
    if bool(driver.find_elements_by_xpath("//strong[text()='Sign In'")):
        print("Break loop, signed out")
        break

    # still in business with no action to buy
    elif bool(driver.find_elements_by_xpath("//*[@id='btn-addCart'][1]")) == False:
        print("Checking")
        time.sleep(random.randint(5, 9))
        driver.get(page_urls[index % length])

    # action
    else:
        print("Attempting to add to cart")
        print(bool(driver.find_elements_by_xpath("//*[@id='btn-addCart'][1]")))
        go_to_checkout()
        
    index += 1