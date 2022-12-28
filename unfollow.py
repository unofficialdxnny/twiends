"""

Note that this script runs directly on Twitter.
This means if you unfollow too many people too fast you will
get rate limited as a first warning and after that your account will be suspended.

Due to this I recommend you to only run this script once a day and unfollow 150-200 people.

use selenium to unfollow everone currently following on twitter

ill probably make it smarter so it only unfollows people you followed using this script or maybe let you choose.


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

driver.get("https://twitter.com/") ## Login
## driver.maximize_window()
wait = WebDriverWait(driver, 100)
os.system('cls')    

print(Colorate.Color(Colors.cyan, banner, True))
