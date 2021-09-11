from math import trunc
import time
from types import coroutine
from typing import Counter
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyperclip
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random
import subprocess



options = Options()
options.add_argument("user-data-dir=/tmp/tarun")
driver = webdriver.Chrome(executable_path = 'chromedriver.exe',chrome_options=options)
driver.get('https://www.coronatracker.com/')




Confirmed = driver.find_elements_by_xpath('//span[@class="mx-2"]')[0].text
print(Confirmed)


Recovered = driver.find_elements_by_xpath('//span[@class="mx-2"]')[2].text
print(Recovered)


Deaths = driver.find_elements_by_xpath('//span[@class="mx-2"]')[4].text
print(Deaths)

