# Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime as dt
from time import sleep
import pyttsx3
#Configuring the browser
browser = webdriver.Chrome()
browser.maximize_window()
# Setting the URL of the Website
url = "https://resonancewarangal.com/liveclasses/home/my_courses"
Creds = 'JAB212119'
# This function Logs in to the user's account using the credentials given 
def LogIn():
    browser.get(url)
    urname = browser.find_element_by_xpath('//*[@id="login-email"]') #Username of mine
    passwd = browser.find_element_by_xpath('/html/body/section[3]/div/div/div/div/div[1]/form/div[1]/div/div[2]/input') #password 
    btn = browser.find_element_by_xpath('/html/body/section[3]/div/div/div/div/div[1]/form/div[2]/button') #Button to login
    urname.send_keys(Creds) #username
    passwd.send_keys(Creds) #password
    btn.click() # button is clicked


# Defining the Speak function to reply me
engine = pyttsx3.init('sapi5')
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Join():
    LogIn()
    Math_btn = browser.find_element_by_xpath('//*[@id="JoinLink"]').get_attribute("href")
    browser.get(Math_btn)
    sleep(5)
    speak('Joined')
Join()
