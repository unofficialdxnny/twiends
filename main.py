"""
Twitter Followers script written in python.
This script automates the twiends website to surpass the hustle
of clicking the follow button upto 400 times.

By @unofficialdxnny (Danial Ahmed)


NOTE THIS SCRIPT DOESNT WORK AS INTENDED. USE "latest.py" start a UI script.

i dont currently have time to fix this script. if you want you can create a PR and upload the headless edition

The only problem is to fix the login xpath and put into correct places :)
"""

from pystyle import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
import sys

import os
import json



banner = '''

     ███████████                  ███                          █████        
    ░█░░░███░░░█                 ░░░                          ░░███         
    ░   ░███  ░  █████ ███ █████ ████   ██████  ████████    ███████   █████ 
        ░███    ░░███ ░███░░███ ░░███  ███░░███░░███░░███  ███░░███  ███░░  
        ░███     ░███ ░███ ░███  ░███ ░███████  ░███ ░███ ░███ ░███ ░░█████ 
        ░███     ░░███████████   ░███ ░███░░░   ░███ ░███ ░███ ░███  ░░░░███
        █████     ░░████░████    █████░░██████  ████ █████░░████████ ██████ 
       ░░░░░       ░░░░ ░░░░    ░░░░░  ░░░░░░  ░░░░ ░░░░░  ░░░░░░░░ ░░░░░░  
                                                                        
                            b̷y̷ u̷n̷o̷f̷f̷i̷c̷i̷a̷l̷d̷x̷n̷n̷y̷

'''






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

print(Colorate.Color(Colors.cyan, banner, True))

sleep(10)    

if driver.current_url == 'https://twiends.com/':
    print(Colorate.Color(Colors.green, 'Loading Up...', True))
    sign_in_with_twitter = driver.find_element(By.XPATH, '//*[@id="body"]/div[2]/div/div/div[2]/div[2]/div/a')
    sign_in_with_twitter.click()
    if 'https://api.twitter.com/' in driver.current_url:
        print(Colorate.Color(Colors.green, 'Attempting to login...', True))
        sleep(2)
        s_in = driver.find_element(By.XPATH, '//*[@id="allow"]').click()
        
        if 'twitter.com/i/' in driver.current_url:
            sleep(3)
            email_field = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input')
            
            email_field.send_keys(data["username"])
            
            password_field = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            
            
            password_field.send_keys(data["password"])
            
            
            sign_in = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div')
            
            sign_in.click()
            
            os.system('cls')
            
            print(Colorate.Color(Colors.cyan, banner, True))
            
            sleep(2)
        
            
        if driver.current_url != 'https://twiends.com/home':
            driver.get('https://twiends.com/home')
            if driver.current_url == 'https://twiends.com/home':
                driver.refresh()
            
for x in range(35):
    sleep(5)
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
    
    driver.find_element(By.XPATH, f'//*[@id="Refresh"]').click()
    sleep(5)
    
                    
