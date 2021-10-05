#####################
# IMPORTING MODULES #
##################### 

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from difflib import get_close_matches
import speech_recognition as sr
from playsound import playsound
from selenium import webdriver
from bs4 import BeautifulSoup
from threading import Thread
from random import choice
import pyautogui as pg
from tkinter import *
import webbrowser
import wikipedia
import requests
import datetime
import smtplib
import pyttsx3
import pyjokes
import random
import time
import json
import cv2
import os



#voice txt file
file = open("data/voice.txt", "r")
voice_number = file.readline()
file.close()


#creating pyttsx3 object
engine = pyttsx3.init('sapi5')

#setting properties for pyttsx3 object
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[int(voice_number)].id)
engine. setProperty("rate", 170)

#data directory
cwd = os.getcwd()
dir1 = str(cwd) + "\\Chrome_data\\Soundcloud"
dir2 = str(cwd) + "\\Chrome_data\\YouTube"
Command_dir = str(cwd) + "\\Commands\\index.html"

#browser settings
Soundcloud_options = Options()
Soundcloud_options.add_argument(f"user-data-dir={dir1}")

#browser settings
YouTube_options = Options()
YouTube_options.add_argument(f"user-data-dir={dir2}")


#read username from txt file
file = open("data/user_name.txt", "r") 
user_name = file.readline()
file.close()



####################################### CHAT BOT ####################################################

data = json.load(open('data/chat.json', encoding='utf-8'))
def reply(query):
	if query in data:
		response =  data[query]
	else:
		query = get_close_matches(query, data.keys(), n=2, cutoff=0.6)
		if len(query)==0: return "None"
		return choice(data[query[0]])

	return choice(response)

####################################### SET UP TEXT TO SPEECH #######################################

def speak(text, display=True):

	if display: attachTOframe(text, True)
	engine.say(text)
	engine.runAndWait()

####################################### SET UP SPEECH TO TEXT #######################################

def record(clearChat=True):
	print('\nListening...')
	AITaskStatusLbl['text'] = 'Listening...'
	r = sr.Recognizer()
	r.dynamic_energy_threshold = False
	r.energy_threshold = 4000
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
		said = ""
		AITaskStatusLbl['text'] = 'Waiting...'
		said = r.recognize_google(audio)
		print(f"\nUser said: {said}")
		if clearChat:
			clearChatScreen()
			attachTOframe(said)
	return said.lower()
    
def voiceMedium():
    wishMe()
    while True:
        try:
         q = record()
        except:
            q = record()
        if q == 'None': continue
        else: main(q.lower())

####################################### WISH USER ACCORDING TO TIME #################################

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning " + user_name)

    elif hour>=12 and hour<18:
        speak("Good Afternoon " + user_name)   

    else:
        speak("Good Evening " + user_name)  

    speak("tell me how may I help you")
    speak("if you need help , just say what can you do.")

####################################### ATTACHING BOT/USER CHAT ON CHAT SCREEN ######################

def attachTOframe(text,bot=False):
	if bot:
		botchat = Label(chat_frame,text=text, bg="#810000", fg="white", justify=LEFT, wraplength=250, font=('Montserrat',12, 'bold'))
		botchat.pack(anchor='w',ipadx=5,ipady=5,pady=5)
	else:
		userchat = Label(chat_frame, text=text, bg="#CE1212", fg='white', justify=RIGHT, wraplength=250, font=('Montserrat',12, 'bold'))
		userchat.pack(anchor='e',ipadx=2,ipady=2,pady=5)

####################################### CLEAR CHAT SCREEN ###########################################

def clearChatScreen():
	for wid in chat_frame.winfo_children():
		wid.destroy()

####################################### SWITCHING BETWEEN FRAMES ####################################

def raise_frame(frame):
	frame.tkraise()
	clearChatScreen()


####################################### TASK/COMMAND HANDLER ########################################
def isContain(txt, lst):
	for word in lst:
		if word in txt:
			return True
	return False

def main(text):

        file = open("data/voice.txt", "r")
        voice_number = file.readline()
        engine.setProperty('voice', voices[int(voice_number)].id)

        ############### Commands list ###############
       
        #Commands #I#
        if 'what can you do' in text:
            speak('Here is the Commands list')
            webbrowser.open("file://" + Command_dir)

        ############### open sites ###############
    
        #open wikipedia #A#
        elif 'open wikipedia' in text:
            webbrowser.open("https://www.wikipedia.org/")
            speak("opening wikipedia website")

        #open stackoverflow  #A#
        elif 'open stack overflow' in text:
            speak("Here you go to Stack Over flow. Happy coding")
            webbrowser.open("https://www.stackoverflow.com") 

        #open github  #A#
        elif 'open github' in text:
            speak("Okay!")
            webbrowser.open("https://github.com/") 
            speak("opening github website")  
      
        #open facebook  #A#
        elif 'open facebook' in text:
            speak("Okay!")
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook website")

        #open telegram #A#
        elif 'open telegram' in text:
            speak("Okay!")
            webbrowser.open("https://web.telegram.org/z/")
            speak("opening telegram website")            
        
        #open and search on Soundcloud  #I#
        elif 'soundcloud' in text:
         try:
            driver = webdriver.Chrome(executable_path = 'chromedriver.exe',chrome_options=Soundcloud_options)

            speak('What do you want to search?')

            search_soundcloud = record(False)
            attachTOframe(search_soundcloud)
            
            driver.get('https://soundcloud.com/search/sounds?q=' + search_soundcloud)
           
            while True:
             if 'Sorry, something went wrong.' in driver.page_source:
              play_btn = driver.find_elements_by_xpath('//li[@class="searchList__item"]/div[@class="searchItem"]/div[@class="sound searchItem__trackItem track streamContext"]/div/div[@class="sound__content"]/div[@class="sound__header sc-mb-1.5x sc-px-2x"]/div/div/div/a')
              play_btn[0].click()                 
             try:
              play_btn = driver.find_elements_by_xpath('//li[@class="searchList__item"]/div[@class="searchItem"]/div[@class="sound searchItem__trackItem track streamContext"]/div/div[@class="sound__content"]/div[@class="sound__header sc-mb-1.5x sc-px-2x"]/div/div/div/a')
              play_btn[0].click()
              break
             except:
                pass
            
            while True: 
                soundcloud = record(False)   
                attachTOframe(soundcloud)
                if 'next' in soundcloud:
                    next_btn = driver.find_element_by_xpath('//div[@class="playControls__elements"]/button[@class="skipControl sc-ir playControls__control playControls__next skipControl__next"]')
                    next_btn.click()
            
                elif 'exit' in soundcloud:
                    driver.close()
                    break
              
                else:
                   break
         except:
              try:
                  driver.close()
              except:
                  pass
              #For handle errors
              speak('Something went wrong Please check your internet connection and try again')

        #open and search on YouTube #I#
        elif 'youtube' in text:
          try:
                driver = webdriver.Chrome(executable_path = 'chromedriver.exe',chrome_options=YouTube_options)
                #Get youtube url
                driver.get('https://www.youtube.com/')
                #put text on search box
                search_form = driver.find_element_by_xpath('//form[@class="style-scope ytd-searchbox"][@id="search-form"]/div/div/input')
                speak('Okay what do you want to search?')
                User_search = record(False)
                attachTOframe(User_search)
                search_form.send_keys(User_search)
                search_button = driver.find_element_by_xpath('//button[@class="style-scope ytd-searchbox"][@id="search-icon-legacy"]')
                search_button.click()
                speak('Here is the results')

          except:
                #For handle errors
                speak('Something went wrong Please check your internet connection and try again')

        #Speed Test from speedtest.net #I#
        elif isContain(text, ['net speed','speed test' 'internet speed']):
            speak('Testing the speed of your internet connection.')
            try:
                driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
                driver.get('https://www.speedtest.net')
                try:
                    GO_btn = driver.find_element_by_xpath('//span[@class="start-text"]')
                    GO_btn.click()
                    time.sleep(2)
                except:
                    pass

                while True:
                    PING  = driver.find_element_by_xpath('//span[@class="result-data-large number result-data-value ping-speed"]').text
                    DOWNLOAD = driver.find_element_by_xpath('//span[@class="result-data-large number result-data-value download-speed"]').text
                    UPLOAD = driver.find_element_by_xpath('//span[@class="result-data-large number result-data-value upload-speed"]').text
                    if PING != ' ' and DOWNLOAD != ' ' and UPLOAD!= ' ':
                        break

                speak('your Ping speed is ' + PING)
                speak('your Download  speed is ' + DOWNLOAD)
                speak('your  Upload speed is ' + UPLOAD)
                driver.close()
            except:
                #For handle errors
                speak('Something went wrong Please check your internet connection and try again')

        #Corona Tracker from coronatracker.com #I#
        elif isContain(text, ['corona tracker','covid tracker','corona statistics', 'covid statistics']):
            try:
                speak('which country?')
                #Get country
                country = record(False)
                attachTOframe(country)
                driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
                if country != 'global':
                 driver.get('https://www.coronatracker.com/country/'+country )

                 if 'Page Not Found' in driver.page_source:
                     speak('Country Not Found. Please try again.')
                     driver.close()
                     
                 else:
                  time.sleep(3)

                  speak('Confirmed:')

                  Confirmed = driver.find_element_by_xpath('//div[@class="px-2 text-center"]/p[@class="text-2xl font-bold text-red-600"]').text
                  speak(Confirmed)

                  new_cases = driver.find_element_by_xpath('//div[@class="px-2 text-center"]/p[@class="text-xs font-bold text-red-600"]').text
                  speak(new_cases)
 
                  speak('Recovered:')

                  Recovered = driver.find_element_by_xpath('//div[@class="px-2 text-center"]/p[@class="text-2xl font-bold text-green-600"]').text
                  speak(Recovered)

                  speak('Deaths:')

                  Deaths = driver.find_element_by_xpath('//div[@class="px-2 text-center"]/p[@class="text-2xl font-bold text-gray-600"]').text
                  speak(Deaths)

                  new_deaths = driver.find_element_by_xpath('//div[@class="px-2 text-center"]/p[@class="text-xs font-bold text-gray-600"]').text
                  speak(new_deaths)
                  driver.close()
                else:
                  #If user choose global
                  driver.get('https://www.coronatracker.com/')

                  speak('Confirmed:')

                  Confirmed = driver.find_elements_by_xpath('//span[@class="mx-2"]')[0].text
                  speak(Confirmed)
 
                  speak('Recovered:')

                  Recovered = driver.find_elements_by_xpath('//span[@class="mx-2"]')[2].text
                  speak(Recovered)

                  speak('Deaths:')

                  Deaths =  driver.find_elements_by_xpath('//span[@class="mx-2"]')[4].text
                  speak(Deaths)

                  driver.close()                    
  
            except:
                #For handle errors
                speak('Something went wrong Please check your internet connection and try again')
       
        #Read news from news.google.com #I#
        elif 'read news' in text:                
         try:
            Counter = 0
            speak('Which news you want to hear?')
            attachTOframe('1-Top stories' + '\n' + '2-World' + '\n' + '3-Your local news' + '\n' + '4-Business' + '\n' + '5-Technology' + '\n' + '6-Entertainment' + '\n' + '7-Sports' + '\n' + '8-Science' + '\n' + '9-Health' + '\n' + '0-Search for topics locations and sources ',True)
            #get user choice
            User_choice = record(False)
            attachTOframe(User_choice)
            #to launch chrome browser
            driver = webdriver.Chrome(executable_path = 'chromedriver.exe') 
            
            if User_choice == '1' or 'Top stories' in User_choice or 'top stories' in User_choice:
                #get top stories news url
                driver.get('https://news.google.com/')
                clearChatScreen()
                #Read 10 first news headline
                for i in range(10):
                    if Counter == 4 or Counter == 7:
                        clearChatScreen()
                    #find news headline text
                    news = driver.find_elements_by_xpath('//article[@class=" MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne"]/h3/a')[Counter].text
                    speak(news)
                    Counter +=1
                #close driver
                driver.close()

            elif User_choice == '2' or 'World' in User_choice or 'world' in User_choice:
                #get world news url (https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US:en)
                driver.get('https://b2n.ir/q41179')
                clearChatScreen()
                #Read 10 first news headline
                for i in range(10):
                    if Counter == 4 or Counter == 7:
                        clearChatScreen()                    
                    #find news headline text
                    news = driver.find_elements_by_xpath('//article[@class=" MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne"]/h3/a')[Counter].text
                    speak(news)
                    #go to next news headline
                    Counter +=1
                #close driver
                driver.close()

            elif User_choice == '3' or 'Local' in User_choice or 'local' in User_choice:
                #get local news url (https://news.google.com/topics/CAAqHAgKIhZDQklTQ2pvSWJHOWpZV3hmZGpJb0FBUAE/sections/CAQiTkNCSVNORG9JYkc5allXeGZkakpDRUd4dlkyRnNYM1l5WDNObFkzUnBiMjV5Q2hJSUwyMHZNR1owYkhoNkNnb0lMMjB2TUdaMGJIZ29BQSowCAAqLAgKIiZDQklTRmpvSWJHOWpZV3hmZGpKNkNnb0lMMjB2TUdaMGJIZ29BQVABUAE?hl=en-US&gl=US&ceid=US:en)
                driver.get('https://b2n.ir/h39264')
                clearChatScreen()
                #Read 10 first news headline
                for i in range(10):
                    if Counter == 4 or Counter == 7:
                        clearChatScreen()                    
                    #find news headline text
                    news = driver.find_elements_by_xpath('//article[@class=" MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne"]/h3/a')[Counter].text
                    speak(news)
                    #go to next news headline
                    Counter +=1
                #close driver
                driver.close()

            elif User_choice == '4' or 'Business' in User_choice or 'business' in User_choice:
                #get business news url (https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US:en)
                driver.get('https://b2n.ir/m52571')
                clearChatScreen()
                #Read 10 first business news
                for i in range(10):
                    if Counter == 4 or Counter == 7:
                        clearChatScreen()                    
                    #find news headline text
                    news = driver.find_elements_by_xpath('//article[@class=" MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne"]/h3/a')[Counter].text
                    speak(news)
                    #go to next news headline
                    Counter +=1
                #close driver
                driver.close()

            elif User_choice == '5' or 'Technology' in User_choice or 'technology' in User_choice:
                 #get technology news url (https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US:en)
                driver.get('https://b2n.ir/x71855')
                clearChatScreen()
                #Read 10 first technology news
                for i in range(10):
                    if Counter == 4 or Counter == 7:
                        clearChatScreen()                    
                    #find news headline text
                    news = driver.find_elements_by_xpath('//article[@class=" MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne"]/h3/a')[Counter].text
                    speak(news)
                    #go to next news headline
                    Counter +=1
                #close driver
                driver.close()

            elif User_choice == '6' or 'Entertainment' in User_choice or 'entertainment' in User_choice:
                #get entertainment news url (https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US:en)
                driver.get('https://b2n.ir/x88215')
                clearChatScreen()
                #Read 10 first entertainment news
                for i in range(10):
                    if Counter == 4 or Counter == 7:
                        clearChatScreen()                    
                    #find news headline text
                    news = driver.find_elements_by_xpath('//article[@class=" MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne"]/h3/a')[Counter].text
                    speak(news)
                    #go to next news headline
                    Counter +=1
                #close driver
                driver.close()

            elif User_choice == '7' or 'Sports' in User_choice or 'sports' in User_choice:
                #get sports news url (https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US:en)
                driver.get('https://b2n.ir/m81691')
                clearChatScreen()
                #Read 10 first sports news
                for i in range(10):
                    if Counter == 4 or Counter == 7:
                        clearChatScreen()                    
                    #find news headline text
                    news = driver.find_elements_by_xpath('//article[@class=" MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne"]/h3/a')[Counter].text
                    speak(news)
                    #go to next news headline
                    Counter +=1
                #close driver
                driver.close()

            elif User_choice == '8' or 'Science' in User_choice or 'science' in User_choice:
                #get science news url (https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US:en)
                driver.get('https://b2n.ir/h50778')
                clearChatScreen()
                #Read 10 first science news
                for i in range(10):
                    if Counter == 4 or Counter == 7:
                        clearChatScreen()                    
                    #find news headline text
                    news = driver.find_elements_by_xpath('//article[@class=" MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne"]/h3/a')[Counter].text
                    speak(news)
                    #go to next news headline
                    Counter +=1
                #close driver
                driver.close()

            elif User_choice == '9' or 'Health' in User_choice or 'health' in User_choice:
                #get health news url (https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US:en)
                driver.get('https://b2n.ir/w06918')
                clearChatScreen()
                #Read 10 first health news
                for i in range(10):
                    if Counter == 4 or Counter == 7:
                        clearChatScreen()                    
                    #find news headline text
                    news = driver.find_elements_by_xpath('//article[@class=" MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne"]/h3/a')[Counter].text
                    speak(news)
                    #go to next news headline
                    Counter +=1
                #close driver
                driver.close()

            elif User_choice == '0' or 'Search' in User_choice or 'search' in User_choice:
                speak('What do you want to search?')
                User_search = record(False)
                #get url
                driver.get('https://news.google.com')
                clearChatScreen()
                #find search box
                Search_box = driver.find_element_by_xpath('//input[@aria-label="Search"][@type="text"][@class="Ax4B8 ZAGvjd"]')      
                #put User_search to search box
                Search_box.send_keys(User_search)
                #Enter
                Search_box.send_keys(Keys.ENTER)
                #go to search result url
                driver.get(driver.current_url)
                #Read 10 first news
                for i in range(10):
                    if Counter == 4 or Counter == 7:
                        clearChatScreen()                    
                    #find news headline text
                    news = driver.find_elements_by_xpath('//article[@class=" MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne"]/h3/a')[Counter].text
                    speak(news)
                    #go to next news headline
                    Counter +=1
                #close driver
                driver.close()
            
            else:
                #If the user said wrong 
                driver.close()
                speak('Please say a number or topic name')
         except:
             #For handle errors
             speak('Something went wrong Please check your internet connection and try again')
      

        ############### entertainment  ###############

        #Roll a dice or roll two dice #I#
        elif 'roll two die' in text or 'two dice'in text:
           #Random number
           dice1 =  random.choice(['One','Two','Three','Four','Five','Six'])
           dice2 =  random.choice(['One','Two','Three','Four','Five','Six'])
           #Random answer
           say = random.choice([('its ' + dice1 + ' and ' + dice2) , (dice1 + ' and ' + dice2) ,('its '+ dice1 + ' and ' + dice2 + ' this time') , ('ok... '+ dice1 + ' and ' + dice2)])
           speak('Rolling...')
           time.sleep(1)
           speak(say)
        elif 'dice' in text:
           #Random number
           dice =  random.choice(['One','Two','Three','Four','Five','Six'])
           #Random answer
           say = random.choice(['its '+ dice,dice,'its '+ dice + ' this time','ok... '+dice])
           speak('Rolling...')
           time.sleep(1)
           speak(say)
   
        #Flip a coin #I#
        elif 'coin' in text:
           #Random choice
           coin =  random.choice(['Tails','Heads'])
           #Random answer
           say = random.choice(['its '+ coin,coin,'its '+ coin + ' this time'])
           speak(say)

        #What is your favorite color #I#
        elif 'your favorite color' in text or 'your favourite colour' in text:
            #Random color
            color = random.choice(['Red','Yellow' ,'Blue' , 'Orange' , 'Green' , 'Pink' , 'Purple' , 'Black' , 'White'])
            speak("software doesn't usually get to choose one, but i'll say," + color + ",""what's your's?")
            #Get user color
            user_color = record(False)
            attachTOframe(user_color)
            if user_color == 'red' :
                speak('Red is the traditional color of warning and danger, and is therefore often used on flags.')
            elif user_color == 'orange':
                speak("I like orange too,it's the symbol of the fall season")
            elif user_color == 'yellow':
                speak("Yellow is a common color of flowers.")
            elif user_color == 'green':
                speak("Nice ,Green is color of nature and life.")
            elif user_color == 'blue':
                speak("Blue , color like the ocean or the sky")
            elif user_color == 'purple':
                speak("The color purple has been associated with royalty, power and wealth")
            elif user_color == 'black':
                speak("In 2014 , scientists discovered Vantablack. it's the darkest material on Earth, made of carbon fiber tubes that absorb 99.965% of all light!")
            elif user_color == 'white':
                speak("White is an important symbolic color in most religions and cultures, usually because of its association with purity. ")
            elif user_color == 'pink':
                speak("Pink is the color most commonly associated with sweet tastes ")
            else:
                speak("Nice Choice!")

        #Tell me a joke #I#
        elif 'tell me a joke' in text or 'say a joke' in text:
        
            speak((pyjokes.get_joke()))
       
        #Repeat after me #I#
        elif 'repeat after me' in text:
            speak('okay')
            Speak_user = record(False)
            attachTOframe(Speak_user)
            speak(Speak_user)
        
        #Rock Paper Scissors #A#
        elif isContain(text, ['rock','paper','scissors']):
        
            speak("Start Rock Paper Scissors game")
            while True:
                speak("choice one (rock, paper, scissors) ")
                user_action = record(False)
                attachTOframe(user_action)
                possible_actions = ["rock", "paper", "scissors"]
                computer_action = random.choice(possible_actions)


                if user_action == computer_action:
                    speak(f"Both players selected {user_action}. It's a tie!")
            
                elif "rock" in user_action:
                    if computer_action == "scissors":
                        speak("Rock smashes scissors! You win!")
                
                    else:
                        speak("Paper covers rock! You lose.")
                
                elif "paper" in user_action:
                    if computer_action == "rock":
                        speak("Paper covers rock! You win!")
                
                    else:
                        speak("Scissors cuts paper! You lose.")
                
                elif "scissors" in user_action:
                    if computer_action == "paper":
                        speak("Scissors cuts paper! You win!")
                
                    else:
                        speak("Rock smashes scissors! You lose.")
                

                speak("Play again? (yes/no): ")
                play_again = record(False)
                attachTOframe(play_again)
                if 'yes' in play_again or 'y' in play_again or 'play again' in play_again:
                    continue
                else:
                    speak('okay Good game')
                    break

        #space game #A#
        elif 'space' in text and 'game' in text:
            import gamespace

        ############### ###############  ###############  ###############
        #temperature #A#
        elif 'temperature' in text:
            search = "temperature"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temperature = data.find("div", class_ = "BNeawe").text
            speak(f"The Temperature outside is {temperature}")   
        
        #date #A#
        elif 'date' in text:
            t_date = datetime.datetime.now()
            speak(t_date.strftime('%D'))
 
        #time #A#
        elif 'time' in text:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"the time is {strTime}")

        #take picture #I#
        elif isContain(text, ['take picture','take pic','take a picture','take a pic']):
            videoCaptureObject = cv2.VideoCapture(0)
            result = True
            while(result):
                ret,frame = videoCaptureObject.read()
                cv2.imwrite("Picture.jpg",frame)
                result = False
            videoCaptureObject.release()
            cv2.destroyAllWindows()
            speak('Done, your picture saved on Picture.jpg')

        #write a note #A#
        elif "write" in text and 'note' in text:
            speak("What should i write")
            note = record(False)
            attachTOframe(note)
            file = open('Note.txt', 'w')
            file.write(note)
            speak("Your note saved on Note.txt")
        
        #take screenshot #A#
        elif 'take screenshot' in text:
            screenshot = pg.screenshot()
            screenshot.save("Screenshot.png")
            speak("Screenshot Taken Successfully, its saved on Screenshot.png")
        
        #open notepad #A#
        elif 'notepad' in text:
            speak("openning Notepad")
            path=("C:\\Windows\\system32\\notepad.exe")
            os.startfile(path)

        #open cmd #A#
        elif 'cmd' in text:
            speak("openning Command Prompt ")
            os.system("start cmd")

        #send email #A#
        elif 'send email' in text:
            try:

                file = open("data\\Email.txt", "r")
                Email = file.readline()
                file.close()

                if Email == '':
                    speak('enter your Email here')
                    os.system('data\\Email.txt')
                    speak('enter your Password here')
                    os.system('data\\Password.txt')
                
                speak("What should I say?")
                content = record(False)
                attachTOframe(content)



                speak('send Email to who')
                os.system('data\\to.txt')

                file = open("data\\Email.txt", "r")
                Email = file.readline()
                file.close()

                file = open("data\\Password.txt", "r")
                Password = file.readline()
                file.close()

                file = open("data\\to.txt", "r")
                to = file.readline()
                file.close()

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login(Email, Password)
                server.sendmail(Email, to, content)
                server.quit()

                
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Username and Password not accepted.")  

        #control volume #I#
        elif 'volume up' in text:
            pg.press("volumeup")
            pg.press("volumeup")
            pg.press("volumeup")
        elif 'volume down' in text:
            pg.press("volumedown")
            pg.press("volumedown")
            pg.press("volumedown")
        elif 'volume mute' in text:
            pg.press("volumemute")
         
        #Shutdown #I#
        elif isContain(text, ['sign out','signout','logoff']):
         speak('Are you sure you want to logout your system?')
         #Get confirmed
         Confirmed = record(False)
         if 'yes' in Confirmed or 'Yes' in Confirmed:
            speak('okay')
            #Sign out Windows
            os.system("shutdown -l")
        elif "shutdown" in text or "shut down" in text:
            speak('Are you sure you want to shutdown your system?')
            #Get confirmed
            Confirmed = record(False)
            if 'yes' in Confirmed or 'Yes' in Confirmed:
                speak('okay')
                #Shutdown Windows
                os.system("shutdown -s")
        elif "restart" in text:
            speak('Are you sure you want to restart your system?')
            #Get confirmed
            Confirmed = record(False)
            if 'yes' in Confirmed or 'Yes' in Confirmed:
                speak('okay')
                #Restart Windows
                os.system("shutdown -r")    
            
        #Learn how to say my name #I#
        elif 'learn my name' in text:
            speak("Okay, what's your name?")
            #Get user name
            user_name = record(False)
            attachTOframe(user_name)
            speak('Do You Want  Call You, ' + user_name + '?')
            #Get user confirmed
            Confirmed = record(False)
            attachTOframe(Confirmed)
            if Confirmed == 'yes':
             speak('Okay from now on, I call you ' + user_name)
             file = open('data/user_name.txt', 'r+')
             #Remove last user name from file
             file.truncate(0)
             #Write user name in file
             file.write(user_name)
             file.close()

        #change voice #I#
        elif 'change' in text and 'voice' in text:
           
            speak('Okay')
            if voice_number == '0':
                file = open('data/voice.txt', 'r+')
                #Remove last number from file
                file.truncate(0)
                #Write number in file
                file.write('1')
            else:
                file = open('data/voice.txt', 'r+')
                #Remove last number from file
                file.truncate(0)
                #Write number in file
                file.write('0')                    

        #Alarm #I#
        elif 'set' in text and 'alarm' in text:
         try:
            speak('Set the alarm for when?')
            alarm_time = record(False)
            attachTOframe(alarm_time)
               

            if ":" in alarm_time:
               
                if len(alarm_time) == 4:
                            driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
                            driver.get('https://kukuklok.com/')
                            sound = driver.find_element_by_xpath('//div[@class="clock_button"][@id="choose_sound_right"]')
                            sound.click()
                            sound.click()     
                            hour_bt = driver.find_element_by_xpath('//div[@id="button_plus_hour"][@class="clock_button"]')
                            min_bt = driver.find_element_by_xpath('//div[@id="button_plus_min"][@class="clock_button"]') 
                            h = alarm_time[0]
                            m = alarm_time[2:]
                            for i in range(int(h)):
                                hour_bt.click()
                            for i in range(int(m)):
                                min_bt.click()     
                            set_Alarm = driver.find_element_by_xpath('//div[@id="set_alarm_button"][@class="button"]')
                            set_Alarm.click()
                            driver.minimize_window()
                            speak('Done')

                elif len(alarm_time) == 5:

                        driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
                        driver.get('https://kukuklok.com/')
                        sound = driver.find_element_by_xpath('//div[@class="clock_button"][@id="choose_sound_right"]')
                        sound.click()
                        sound.click()     
                        hour_bt = driver.find_element_by_xpath('//div[@id="button_plus_hour"][@class="clock_button"]')
                        min_bt = driver.find_element_by_xpath('//div[@id="button_plus_min"][@class="clock_button"]') 
                        h = alarm_time[:2]
                        m = alarm_time[3:]
                        for i in range(int(h)):
                            hour_bt.click()
                        for i in range(int(m)):
                            min_bt.click()     
                        set_Alarm = driver.find_element_by_xpath('//div[@id="set_alarm_button"][@class="button"]')
                        set_Alarm.click()
                        driver.minimize_window()
                        speak('Done')

            elif ":" not in alarm_time:
           
             if len(alarm_time) == 3:
                driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
                driver.get('https://kukuklok.com/')
                sound = driver.find_element_by_xpath('//div[@class="clock_button"][@id="choose_sound_right"]')
                sound.click()
                sound.click()     
                hour_bt = driver.find_element_by_xpath('//div[@id="button_plus_hour"][@class="clock_button"]')
                min_bt = driver.find_element_by_xpath('//div[@id="button_plus_min"][@class="clock_button"]') 
                h = alarm_time[0]
                m = alarm_time[1:]
                for i in range(int(h)):
                 hour_bt.click()
                for i in range(int(m)):
                 min_bt.click()     
                set_Alarm = driver.find_element_by_xpath('//div[@id="set_alarm_button"][@class="button"]')
                set_Alarm.click()
                driver.minimize_window()
                speak('Done')
          
             elif len(alarm_time) == 4:
                driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
                driver.get('https://kukuklok.com/')
                sound = driver.find_element_by_xpath('//div[@class="clock_button"][@id="choose_sound_right"]')
                sound.click()
                sound.click()     
                hour_bt = driver.find_element_by_xpath('//div[@id="button_plus_hour"][@class="clock_button"]')
                min_bt = driver.find_element_by_xpath('//div[@id="button_plus_min"][@class="clock_button"]') 
                h = alarm_time[:2]
                m = alarm_time[2:]
                for i in range(int(h)):
                 hour_bt.click()
                for i in range(int(m)):
                 min_bt.click() 
                set_Alarm = driver.find_element_by_xpath('//div[@id="set_alarm_button"][@class="button"]')
                set_Alarm.click()
                driver.minimize_window()
                speak('Done')
            
            else:
                speak('please just say time')
         except:
                 
              #For handle errors
              speak('Something went wrong Please check your internet connection and try again')  
              driver.close()
       
        #playlist #I#
        elif isContain(text, ['music','playlist','song']):
            music_dir = 'playlist'
            songs = os.listdir(music_dir)
            if songs == []:
                os.startfile('playlist')
                speak("I didn't find any song, please move your playlist here.")
            else:
                counter = 0
                for li in songs:
                    s = (songs[counter])
                    playsound(f'playlist\\{s}')
                    counter +=1      

        #Exit #A#
        elif isContain(text, ['exit','goodbye','quit','bye','close']):          
          speak('Goodbye')
          root.destroy()

        #wikipedia summary #I# 
        elif isContain(text, ['who is','what is',"what's","who's",'meaning' ]):

                text = text.replace('who is' , '')
                text = text.replace('what is' , '')
                text = text.replace("what's" , '')
                text = text.replace("who's" , '')
                text = text.replace('who is the' , '')
                text = text.replace('what is the' , '')
                text = text.replace("who's the" , '')
                text = text.replace("what's the" , '')
                text = text.replace("meaning of" , '')
                text = text.replace("meaning" , '')


                try:
                    speak(wikipedia.summary(text, sentences=1))
                except Exception as e:
                    webbrowser.open("https://www.google.com/search?q=" + text)
                    speak("Here's what I found on the web... ")

        #search on google #I#
        else:
         result = reply(text)
         if result != "None": speak(result)
         else:
          webbrowser.open("https://www.google.com/search?q=" + text)
          speak("Here's what I found on the web... ")
       


############################################## GUI #############################################


root = Tk()
root.title('Eve')

root.geometry('400x640+1320+200')
root.resizable(False, False) 

root.iconphoto(False, PhotoImage(file='images/icon.png'))
root.pack_propagate(0)
root1 = Frame(root, bg='#170903')

for f in (root1,):
    f.grid(row=0, column=0, sticky='news')	
chat_frame = Frame(root1, width=380,height=551,bg='#170903')
chat_frame.pack(padx=10)
chat_frame.pack_propagate(0)
bottomFrame = Frame(root1,height=100)
bottomFrame.pack(fill=X, side=BOTTOM)
VoiceModeFrame = Frame(bottomFrame)
VoiceModeFrame.pack(fill=BOTH)

box = PhotoImage(file='images/box.png')
cbl = Label(VoiceModeFrame, fg='white', image=box,)
cbl.pack(pady=17)
AITaskStatusLbl = Label(VoiceModeFrame, text='Waiting...', fg='white', bg='#940A0A', font=('montserrat', 16))
AITaskStatusLbl.place(x=140,y=32)

Thread(target=voiceMedium).start()

raise_frame(root1)
root.mainloop()