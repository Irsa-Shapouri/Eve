#####################
# IMPORTING MODULES #
##################### 

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from difflib import get_close_matches
import speech_recognition as sr
from selenium import webdriver
from threading import Thread
from random import choice
from tkinter import *
import datetime
import pyjokes
import pyttsx3
import random
import json
import time
import os
import sys

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

#browser settings
options = Options()
options.add_argument("user-data-dir=/tmp/tarun")

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

def record(clearChat=True, iconDisplay=True):
	print('\nListening...')
	AITaskStatusLbl['text'] = 'Listening...'
	r = sr.Recognizer()
	r.dynamic_energy_threshold = False
	r.energy_threshold = 4000
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
		said = ""
		try:
			AITaskStatusLbl['text'] = ' Waiting...'
			said = r.recognize_google(audio)
			print(f"\nUser said: {said}")
			if clearChat:
				clearChatScreen()
			if iconDisplay: Label(chat_frame,  bg='#121010').pack(anchor='e',pady=0)
			attachTOframe(said)
		except Exception as e:
			print(e)
			if "connection failed" in str(e):
				speak("Your System is Offline...",)
			return 'None'
	return said.lower()
def voiceMedium():
    wishMe()
    while True:
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

def main(text):

        file = open("data/voice.txt", "r")
        voice_number = file.readline()
        engine.setProperty('voice', voices[int(voice_number)].id)
       
        #Read news
        if 'read news' in text:                
         try:
            Counter = 0
            engine. setProperty("rate", 180)
            speak('Okay, choose one' + '\n' + '1-Top stories' + '\n' + '2-World' + '\n' + '3-Your local news' + '\n' + '4-Business' + '\n' + '5-Technology' + '\n' + '6-Entertainment' + '\n' + '7-Sports' + '\n' + '8-Science' + '\n' + '9-Health' + '\n' + '0-Search for topics locations and sources ')
            engine. setProperty("rate", 170)
            #get user choice
            User_choice = record(False)
            #to launch chrome browser
            driver = webdriver.Chrome(executable_path = 'chromedriver.exe') 
            
            if User_choice == '1' or 'Top stories' in User_choice or 'top stories' in User_choice:
                #get top stories news url
                driver.get('https://news.google.com/')
                clearChatScreen()
                #Read 10 first news headline
                for i in range(10):
                    if Counter == 5:
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
                    if Counter == 5:
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
                    if Counter == 5:
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
                    if Counter == 5:
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
                    if Counter == 5:
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
                    if Counter == 5:
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
                    if Counter == 5:
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
                    if Counter == 5:
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
                    if Counter == 5:
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
                    if Counter == 5:
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
      
        #Shutdown
        elif "log off" in text or "sign out" in text or "signout" in text or "logoff" in text:
         speak('Are you sure you want to logout your Windows Computer?')
         #Get confirmed
         Confirmed = record(False)
         if 'yes' in Confirmed or 'Yes' in Confirmed:
            speak('okay')
            #Sign out Windows
            os.system("shutdown -l")
        elif "shutdown" in text or "shut down" in text:
            speak('Are you sure you want to shutdown your Windows Computer?')
            #Get confirmed
            Confirmed = record(False)
            if 'yes' in Confirmed or 'Yes' in Confirmed:
                speak('okay')
                #Shutdown Windows
                os.system("shutdown -s")
        elif "restart" in text:
            speak('Are you sure you want to restart your windows Computer?')
            #Get confirmed
            Confirmed = record(False)
            if 'yes' in Confirmed or 'Yes' in Confirmed:
                speak('okay')
                #Restart Windows
                os.system("shutdown -r")    
            
        #Roll a die or roll two dice
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
   
        #Flip a coin
        elif 'coin' in text:
           #Random choice
           coin =  random.choice(['Tails','Heads'])
           #Random answer
           say = random.choice(['its '+ coin,coin,'its '+ coin + ' this time'])
           speak(say)

        #What is your favorite color
        elif 'your favorite color' in text or 'your favourite colour' in text:
            #Random color
            color = random.choice(['Red','Yellow' ,'Blue' , 'Orange' , 'Green' , 'Pink' , 'Purple' , 'Black' , 'White'])
            speak("software doesn't usually get to choose one, but i'll say," + color + ",""what's your's")
            #Get user color
            user_color = record(False)
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
                speak("Nice Choice")

        #Tell me a joke
        elif 'tell me a joke' in text or 'say a joke' in text:
        
            speak((pyjokes.get_joke()))
       
        #Learn how to say my name
        elif 'learn my name' in text:
            speak("Okay, what's your name?")
            #Get user name
            user_name = record(False)
            speak('Do You Want  Call You, ' + user_name + '?')
            #Get user confirmed
            Confirmed = record(False)
            if Confirmed == 'yes':
             speak('Okay from now on, I call you ' + user_name)
             file = open('user_name.txt', 'r+')
             #Remove last user name from file
             file.truncate(0)
             #Write user name in file
             file.write(user_name)
             file.close()

        #repeat after me
        elif 'repeat after me' in text:
            speak('okay')
            Speak_user = record(False)
            speak(Speak_user)

        #Soundcloud
        elif 'soundcloud' in text:
         driver = webdriver.Chrome(executable_path = 'chromedriver.exe',chrome_options=options)

         speak('What do you want to search?')

         search_soundcloud = record(False)
        
         driver.get('https://soundcloud.com/search/sounds?q=' + search_soundcloud)
         
         play_btn = driver.find_elements_by_xpath('//li[@class="searchList__item"]/div[@class="searchItem"]/div[@class="sound searchItem__trackItem track streamContext"]/div/div[@class="sound__content"]/div[@class="sound__header sc-mb-1.5x sc-px-2x"]/div/div/div/a')
         play_btn[0].click()

        
         while True: 
            soundcloud = record(False)   
          
            if 'next' in soundcloud:
                next_btn = driver.find_element_by_xpath('//div[@class="playControls__elements"]/button[@class="skipControl sc-ir playControls__control playControls__next skipControl__next"]')
                next_btn.click()
           
            elif 'stop' in soundcloud or 'play' in soundcloud:
                play_btn = driver.find_elements_by_xpath('//div[@class="playControls__elements"]/button[@class="playControl sc-ir playControls__control playControls__play"]')
                play_btn.click()

            elif 'previous' in soundcloud:
                previous_btn = driver.find_elements_by_xpath('//div[@class="playControls__elements"]/button[@class="skipControl sc-ir playControls__control playControls__prev skipControl__previous"]')
                previous_btn.click()  

            elif 'exit' in soundcloud:
                break
            else:
                continue

        #YouTube Search
        elif ('search' in text and 'YouTube' in text):
          try:
                driver = webdriver.Chrome(executable_path = 'chromedriver.exe',chrome_options=options)
                #Get youtube url
                driver.get('https://www.youtube.com/')
                #put text on search box
                search_form = driver.find_element_by_xpath('//form[@class="style-scope ytd-searchbox"][@id="search-form"]/div/div/input')
                speak('Okay what do you want to search?')
                User_search = record(False)
                search_form.send_keys(User_search)
                search_button = driver.find_element_by_xpath('//form[@class="style-scope ytd-searchbox"][@id="search-form"]/button')
                search_button.click()
                speak('Here is the results')

          except:
                #For handle errors
                speak('Something went wrong Please check your internet connection and try again')

        #Speed Test
        elif 'net speed' in text or 'speed test' in text or 'test speed' in text or ('internet' in text and 'speed' in text):
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

        #Corona Tracker#
        elif 'corona tracker' in text or 'covid tracker' in text or 'corona statistics' in text or 'covid statistics' in text:
            try:
                speak('which country?')
                #Get country
                country = record(False)
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
       
        #change voice
        elif 'change' in text and 'voice' in text:
            
            speak('Okay')
            if voice_number == '0':
                file = open('voice.txt', 'r+')
                #Remove last number from file
                file.truncate(0)
                #Write number in file
                file.write('1')
            else:
                file = open('voice.txt', 'r+')
                #Remove last number from file
                file.truncate(0)
                #Write number in file
                file.write('0')                    
          
        #Exit  
        elif 'exit' in text or 'goodbye' in text or 'quit' in text or 'bye' in text:          
         
          speak('Goodbye')
          root.destroy()

        else:
         result = reply(text)
         if result != "None": speak(result)
         else:
            speak("Here's what I found on the web... ")
            driver = webdriver.Chrome(executable_path = 'chromedriver.exe',chrome_options=options)
            driver.get('https://www.google.com/')
            search = driver.find_element_by_name('q')
            search.send_keys(text)
            search.send_keys(Keys.RETURN)


############################################## GUI #############################################

root = Tk()
root.title('CS50x')

root.geometry('400x640+1060+100')
root.resizable(False, False) 

root.iconphoto(False, PhotoImage(file='images/icon.png'))
root.pack_propagate(0)
root1 = Frame(root, bg='#121010')

for f in (root1,):
    f.grid(row=0, column=0, sticky='news')	
chat_frame = Frame(root1, width=380,height=551,bg='#121010')
chat_frame.pack(padx=10)
chat_frame.pack_propagate(0)
bottomFrame = Frame(root1,height=100)
bottomFrame.pack(fill=X, side=BOTTOM)
VoiceModeFrame = Frame(bottomFrame)
VoiceModeFrame.pack(fill=BOTH)

box = PhotoImage(file='images/box.png')
cbl = Label(VoiceModeFrame, fg='white', image=box,)
cbl.pack(pady=17)
AITaskStatusLbl = Label(VoiceModeFrame, text=' Waiting...', fg='white', bg='#940A0A', font=('montserrat', 16))
AITaskStatusLbl.place(x=140,y=32)

Thread(target=voiceMedium).start()

raise_frame(root1)
root.mainloop()
