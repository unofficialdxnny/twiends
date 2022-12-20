from pystyle import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep

import os
import json


try:
    os.system('cls')
    config = open('config.json')
    data = json.load(config)



    options = Options()
    options.page_load_strategy = 'eager'
    options.headless = False
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("detach", True)
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(executable_path='./WebDriver/chromedriver.exe', options=options, service_args=["--verbose", "--log-path=D:\\qc1.log"]) ## Initialise the driver   
    

    driver.get("https://twiends.com/") ## Login
    ## driver.maximize_window()
    wait = WebDriverWait(driver, 100)
    os.system('cls')    

    sleep(2)    
    

    if driver.current_url == 'https://twiends.com/':
        print(Colorate.Color(Colors.green, 'Loading Up...', True))
        sign_in_with_twitter = driver.find_element(By.XPATH, '//*[@id="body"]/div[2]/div/div/div[2]/div[2]/div/a')
        sign_in_with_twitter.click()
        if 'oauth' in driver.current_url:
            print(Colorate.Color(Colors.green, 'Attempting to login...', True))
            email_field = driver.find_element(By.XPATH, '//*[@id="username_or_email"]')
            email_field.send_keys(data["username"])
            password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
            password_field.send_keys(data["password"])
            sign_in = driver.find_element(By.XPATH, '//*[@id="allow"]')
            sign_in.click()
            sleep(2)
            if driver.current_url == 'https://twiends.com/home':
                driver.refresh()
                sleep(5)
                div = 1
                while div != 12:
                    driver.find_element(By.XPATH, f'//*[@id="NewList"]/div[2]/div/div[2]/code').click()
                    sleep(2)
                    driver.find_element(By.XPATH, f'//*[@id="NewList"]/div[3]/div/div[2]/code').click()
                    sleep(2)
                    driver.find_element(By.XPATH, f'//*[@id="NewList"]/div[4]/div/div[2]/code').click()
                    sleep(2)
                    driver.find_element(By.XPATH, f'//*[@id="NewList"]/div[5]/div/div[2]/code').click()
                    sleep(2)
                    driver.find_element(By.XPATH, f'//*[@id="NewList"]/div[6]/div/div[2]/code').click()
                    sleep(2)
                    driver.find_element(By.XPATH, f'//*[@id="NewList"]/div[7]/div/div[2]/code').click()
                    sleep(2)
                    driver.find_element(By.XPATH, f'//*[@id="NewList"]/div[8]/div/div[2]/code').click()
                    sleep(2)
                    driver.find_element(By.XPATH, f'//*[@id="NewList"]/div[9]/div/div[2]/code').click()
                    sleep(2)
                    driver.find_element(By.XPATH, f'//*[@id="NewList"]/div[10]/div/div[2]/code').click()
                    sleep(2)
                    driver.find_element(By.XPATH, f'//*[@id="NewList"]/div[11]/div/div[2]/code').click()
                    sleep(2)
                    driver.find_element(By.XPATH, f'//*[@id="NewList"]/div[12]/div/div[2]/code').click()
                    sleep(2)
except Exception:
    driver.find_element(By.XPATH, f'//*[@id="Refresh"]').click()
    sleep(5)
                    
                    
         