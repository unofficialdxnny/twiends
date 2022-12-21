"""

Note that this script runs directly on Twitter.
This means if you unfollow too many people too fast you will
get rate limited as a first warning and after that your account will be suspended.

Due to this I recommend you to only run this script once a day and unfollow 150-200 people.


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

