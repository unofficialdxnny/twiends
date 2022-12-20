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


config = open(f'config.json')
data = json.load(config)



options = Options()
options.page_load_strategy = 'eager'
options.headless = False
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--log-level=3")
driver = webdriver.Chrome(options=options, service_args=["--verbose", "--log-path=D:\\qc1.log"]) ## Initialise the driver
driver.get("https://accounts.snapchat.com/accounts/login") ## login to snapchat
## driver.maximize_window()
wait = WebDriverWait(driver, 100)

