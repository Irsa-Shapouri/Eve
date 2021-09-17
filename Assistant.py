#در اینجا کتابخانه هارو  وارد می کنیم 
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import subprocess
import pyjokes


#---------------------------------------
#ست پروپرتی: setProperty
# پایتسک3: pyttsx3
#سپی5 : sapi5
#گت پروپرتی : getProperty
#------------------------------------------

#engine :  در حین ساخت موتور مقدار اولیه  (پایتسک3)را فعال میکند تولید و توقف گفتار دریافت و تنظیم ویژگی های موتور گفتار و شروع و توقف حلقه های رویداد
#13: یک برنامه (پایتتسک3) را فراخوانی میکند و کار اصلیش تبدیل که متن وارد شده را به گفتار تبدیل میکند و ماژول (پایتتسک3) دو صدا پشتیبانی میکند که اول زن است و دیگری نر است که توسط (سپی5) برای ویندوز هستش)
engine = pyttsx3.init('sapi5')
# گت پروپرتی مقدار فعلی یک ویژگی موتور را بدست می اورد  اما ست پروپرتی دستور را برای تنظیم ویژگی موتور قرار میدهد و متن گفته شده به استرینگ است 
voices = engine.getProperty('voices')
# print(voices[1].id)
#گت پروپرتی مقدار فعلی یک ویژگی موتور را بدست می اورد  اما ست پروپرتی دستور را برای تنظیم ویژگی موتور قرار میدهد و متن گفته شده به استرینگ است
engine.setProperty('voice', voices[1].id)
engine. setProperty("rate", 170)

options = Options()
options.add_argument("user-data-dir=/tmp/tarun")
file = open("user_name.txt", "r")
user_name = file.readline()
file.close()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Email address', 'Passwords')
    server.sendmail('Email address' ,to, content)
    server.close()

    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning," + user_name)

    elif hour>=12 and hour<18:
        speak("Good Afternoon," + user_name)   

    else:
        speak("Good Evening," + user_name)  

    speak("tell me how may I help you")     


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #===================================================
 
        #1-Set an alarm

        #2-Sending emails
        if 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "example@domain.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Unity buddy. I am not able to send this email") # If you email and password is incorrect.
        #3-Sending Whatsapp massage

        #4-Weather

        #5-Math

        #6-Time zone conversions

        #7-Definitions, synonyms, antonyms, or etymologies of words
           
        #8-Site searches

        #9-Open app

        #10-Play music from system

        #11-Play music from soundcloud


        #12-Identify songs

        #13-Take a picture

        #14-What time is it

        #15-Read news
        elif 'read news' in query or 'Read news' in query:
         try:
            Counter = 0
            speak('Okay, choose one, 1-Top stories , 2-World , 3-Your local news , 4-Business , 5-Technology , 6-Entertainment , 7-Sports , 8-Science , 9-Health , 0-Search for topics locations and sources ')
            #get user choice
            User_choice = takeCommand().lower() 
            #to launch chrome browser
            driver = webdriver.Chrome(executable_path = 'chromedriver.exe') 
            
            if User_choice == '1' or 'Top stories' in User_choice or 'top stories' in User_choice:
                #get top stories news url
                driver.get('https://news.google.com/')
                #Read 10 first news headline
                for i in range(10):
                    #find news headline text
                    news = driver.find_elements_by_xpath('//article[@class=" MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne"]/h3/a')[Counter].text
                    speak(news)
                    Counter +=1
                #close driver
                driver.close()

            elif User_choice == '2' or 'World' in User_choice or 'world' in User_choice:
                #get world news url (https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US:en)
                driver.get('https://b2n.ir/q41179')
                #Read 10 first news headline
                for i in range(10):
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
                #Read 10 first news headline
                for i in range(10):
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
                #Read 10 first business news
                for i in range(10):
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
                #Read 10 first technology news
                for i in range(10):
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
                #Read 10 first entertainment news
                for i in range(10):
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
                #Read 10 first sports news
                for i in range(10):
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
                #Read 10 first science news
                for i in range(10):
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
                #Read 10 first health news
                for i in range(10):
                    #find news headline text
                    news = driver.find_elements_by_xpath('//article[@class=" MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne"]/h3/a')[Counter].text
                    speak(news)
                    #go to next news headline
                    Counter +=1
                #close driver
                driver.close()

            elif User_choice == '0' or 'Search' in User_choice or 'search' in User_choice:
                speak('What do you want to search')
                User_search = takeCommand().lower()
                #get url
                driver.get('https://news.google.com')
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
       
        #16-Shutdown	
        elif "log off" in query or "sign out" in query or "signout" in query or "logoff" in query:
         speak('Are you sure you want to logout your Windows Computer?')
         #Get confirmed
         Confirmed = takeCommand().lower()
         if 'yes' in Confirmed or 'Yes' in Confirmed:
            speak('okay')
            #Sign out Windows
            os.system("shutdown -l")

        elif "shutdown" in query or "shut down" in query:
            speak('Are you sure you want to shutdown your Windows Computer?')
            #Get confirmed
            Confirmed = takeCommand().lower()
            if 'yes' in Confirmed or 'Yes' in Confirmed:
                speak('okay')
                #Shutdown Windows
                os.system("shutdown -s")
     
        elif "restart" in query:
            speak('Are you sure you want to restart your windows Computer?')
            #Get confirmed
            Confirmed = takeCommand().lower()
            if 'yes' in Confirmed or 'Yes' in Confirmed:
                speak('okay')
                #Restart Windows
                os.system("shutdown -r")    
      
        #17-Roll a die or roll two dice
        elif 'roll dice' in query  or 'roll two die' in query or 'two dice'in query:
           #Random number
           dice1 =  random.choice(['One','Two','Three','Four','Five','Six'])
           dice2 =  random.choice(['One','Two','Three','Four','Five','Six'])
           #Random answer
           say = random.choice([('its' + dice1 + 'and,' + dice2) , (dice1 + 'and,' + dice2) ,('its'+ dice1 + 'and,' + dice2 + 'this time') , ('ok...'+ dice1 + 'and,' + dice2)])
           speak('Rolling...,')
           time.sleep(1)
           speak(say)
        elif 'roll a dice' in query  or 'roll a die' in query or 'roll die' in query or 'dice' in query:
           #Random number
           dice =  random.choice(['One','Two','Three','Four','Five','Six'])
           #Random answer
           say = random.choice(['its'+ dice,dice,'its'+ dice + 'this time','ok...'+dice])
           speak('Rolling...,')
           time.sleep(1)
           speak(say)
        
        #18-Flip a coin
        elif 'flip a coin' in query or 'coin' in query or 'flip coin' in query:
           #Random choice
           coin =  random.choice(['Tails','Heads'])
           #Random answer
           say = random.choice(['its'+ coin,coin,'its'+ coin + 'this time'])
           speak(say)
        
        #19-What is your favorite color
        elif 'what is your favorite color' in query or 'what is your favourite colour' in query or "what's your favourite colour" in query or "what's your favourite color" in query:
            #Random color
            color = random.choice(['Red','Yellow' ,'Blue' , 'Orange' , 'Green' , 'Pink' , 'Purple' , 'Black' , 'White'])
            speak("software doesn't usually get to choose one, but i'll say," + color + ",""what's your's")
            #Get user color
            user_color = takeCommand()
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

        #20-Tell me a joke
        elif 'tell me a joke' in query or 'say a joke' in query:
        
            speak((pyjokes.get_joke()))
       
        #21-Learn how to say my name
        elif 'Learn how to say my name' in query or 'learn how to say my name' in query:
            speak("Okay, what's your name")
            #Get user name
            user_name = takeCommand()
            speak('Do You Want  Call You,' + user_name)
            #Get user confirmed
            Confirmed = takeCommand()
            if Confirmed == 'yes' or Confirmed == 'Yes':
             file = open('user_name.txt', 'r+')
             #Remove last user name from file
             file.truncate(0)
             #Write user name in file
             file.write(user_name)
             file.close()

        #22-repeat after me
        elif 'repeat after me' in query:
            speak('okay')
            Speak_user = takeCommand().lower()
            speak(Speak_user)

        #23-Reminder

        #24-YouTube Search
        elif ('search' in query and 'youtube' in query) or ('Search' in query and 'Youtube' in query) or  ('Search' in query and 'YouTube' in query) or  ('search' in query and 'YouTube' in query) or  ('search' in query and 'Youtube' in query):
          try:
            driver = webdriver.Chrome(executable_path = 'chromedriver.exe',chrome_options=options)
            #Get youtube url
            driver.get('https://www.youtube.com/')
            #Click on microphone button
            voice_search = driver.find_element_by_xpath('//button[@aria-label="Search with your voice"][@class="style-scope yt-icon-button"][@id="button"]')
            voice_search.click()
            speak('okay what do you want to search')
            while True:
                #Search with voice
                text = driver.find_element_by_xpath('//div[@id="prompt"][@class="style-scope ytd-voice-search-dialog-renderer"]').text
                if text == 'Listening...':
                    continue
                elif text == "Didn't hear that. Try again.":
                     microphone = driver.find_element_by_xpath('//div[@class="style-scope ytd-voice-search-dialog-renderer"][@id="microphone-circle"][@role="button"]')
                     microphone.click()
                     continue
                else:
                    speak('Here is the results ,if you want to download a video just click on that and say download this video')
                    break
          except:
                #For handle errors
                speak('Something went wrong Please check your internet connection and try again')
     
        #25-YouTube Video Downloader
        elif 'download this video' in query:
            try:
             #Get video url
             url = (driver.current_url)
             #Go to youtube downloader website
             driver.get('https://yt1s.com')
             #Put video url
             search = driver.find_element_by_xpath('//input[@id="s_input"][@type="search"]')
             search.send_keys(url)
             button = driver.find_element_by_xpath('//button[@type="button"][@id="btn-convert"]')
             button.click()
             while True:
                 if 'Get link' in driver.page_source:
                     break
             #3 type of video quality
             Quality1 = driver.find_element_by_xpath('//select[@class="form-control form-control-small"][@id="formatSelect"]/optgroup[@label="mp4"]/option[2]').text
             Quality2 = driver.find_element_by_xpath('//select[@class="form-control form-control-small"][@id="formatSelect"]/optgroup[@label="mp4"]/option[3]').text
             Quality3 = driver.find_element_by_xpath('//select[@class="form-control form-control-small"][@id="formatSelect"]/optgroup[@label="mp4"]/option[4]').text

             speak('choose one : ' + '1:' + Quality1 + '2:' + Quality2 + '3:' + Quality3)
          
             User_choice = takeCommand()
            
             if User_choice == '1':
                 #select quality
                 select = driver.find_element_by_xpath('//select[@class="form-control form-control-small"][@id="formatSelect"]/optgroup[@label="mp4"]/option[2]').click()
                 button = driver.find_element_by_xpath('//button[@class="btn-blue-small form-control"][@id="btn-action"]')
                 button.click()
                 while True:
                  try:
                   #Find and click on download button
                   download = driver.find_element_by_xpath('//a[@id="asuccess"][@class="form-control mesg-convert success"]')
                   download.click()
                   break
                  except:
                   pass
             if User_choice == '2':
                 #select quality
                 select = driver.find_element_by_xpath('//select[@class="form-control form-control-small"][@id="formatSelect"]/optgroup[@label="mp4"]/option[2]').click()
                 button = driver.find_element_by_xpath('//button[@class="btn-blue-small form-control"][@id="btn-action"]')
                 button.click()
 
                 while True:
                  try:
                   #Find and click on download button   
                   download = driver.find_element_by_xpath('//a[@id="asuccess"][@class="form-control mesg-convert success"]')
                   download.click()
                   break
                  except:
                   pass
             if User_choice == '3':
                 #select quality
                 select = driver.find_element_by_xpath('//select[@class="form-control form-control-small"][@id="formatSelect"]/optgroup[@label="mp4"]/option[2]').click()
                 button = driver.find_element_by_xpath('//button[@class="btn-blue-small form-control"][@id="btn-action"]')
                 button.click()
                 
                 while True:
                  try:
                   #Find and click on download button
                   download = driver.find_element_by_xpath('//a[@id="asuccess"][@class="form-control mesg-convert success"]')
                   download.click()
                   break
                  except:
                   pass                                    
            except:
                #For handle errors
                speak('Something went wrong Please check your internet connection and try again')
        
        #26-Speed Test
        elif 'net speed' in query or 'speed test' in query or 'test speed' in query or ('internet' and 'speed') in query:
            speak('Testing the speed of your internet connection')
            try:
                driver = webdriver.Chrome(executable_path = 'chromedriver.exe',chrome_options=options)
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

                speak('your Ping speed is' + PING)
                speak('your Download  speed is' + DOWNLOAD)
                speak('your  Upload speed is' + UPLOAD)
                driver.close()
            except:
                #For handle errors
                speak('Something went wrong Please check your internet connection and try again')

        #27-Corona Tracker
        elif ('corona tracker' or 'covid tracker') in query or ('corona statistics' or 'covid statistics') in query:
            try:
                speak('which country')
                #Get country
                country = takeCommand()
                driver = webdriver.Chrome(executable_path = 'chromedriver.exe',chrome_options=options)
                if country != 'global':
                 driver.get('https://www.coronatracker.com/country/'+country )

                 if 'Page Not Found' in driver.page_source:
                     speak('Country Not Found Please try again')
                     driver.close()
                     
                 else:
                  time.sleep(3)

                  speak('Confirmed')

                  Confirmed = driver.find_element_by_xpath('//div[@class="px-2 text-center"]/p[@class="text-2xl font-bold text-red-600"]').text
                  speak(Confirmed)

                  new_cases = driver.find_element_by_xpath('//div[@class="px-2 text-center"]/p[@class="text-xs font-bold text-red-600"]').text
                  speak(new_cases)
 
                  speak('Recovered')

                  Recovered = driver.find_element_by_xpath('//div[@class="px-2 text-center"]/p[@class="text-2xl font-bold text-green-600"]').text
                  speak(Recovered)

                  speak('Deaths')

                  Deaths = driver.find_element_by_xpath('//div[@class="px-2 text-center"]/p[@class="text-2xl font-bold text-gray-600"]').text
                  speak(Deaths)

                  new_deaths = driver.find_element_by_xpath('//div[@class="px-2 text-center"]/p[@class="text-xs font-bold text-gray-600"]').text
                  speak(new_deaths)
                  driver.close()
                else:
                  #If user choose global
                  driver.get('https://www.coronatracker.com/')

                  speak('Confirmed')

                  Confirmed = driver.find_elements_by_xpath('//span[@class="mx-2"]')[0].text
                  speak(Confirmed)
 
                  speak('Recovered')

                  Recovered = driver.find_elements_by_xpath('//span[@class="mx-2"]')[2].text
                  speak(Recovered)

                  speak('Deaths')

                  Deaths =  driver.find_elements_by_xpath('//span[@class="mx-2"]')[4].text
                  speak(Deaths)

                  driver.close()                    
  
            except:
                #For handle errors
                speak('Something went wrong Please check your internet connection and try again')
      
        #28-Goodbye