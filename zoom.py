# Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime as dt
from time import sleep
browser = webdriver.Chrome()

url = "https://resonancewarangal.com/liveclasses/home/my_courses"
def LogIn():
    browser.get(url)
    urname = browser.find_element_by_xpath('//*[@id="login-email"]') #Username of mine
    passwd = browser.find_element_by_xpath('/html/body/section[3]/div/div/div/div/div[1]/form/div[1]/div/div[2]/input') #password 
    btn = browser.find_element_by_xpath('/html/body/section[3]/div/div/div/div/div[1]/form/div[2]/button') #Button to login
    urname.send_keys('JAB212119') #username
    passwd.send_keys('JAB212119') #password
    btn.click() # button is clicked
# sleep(30)
def mathsJoin():
    LogIn()
    Math_btn = browser.find_element_by_xpath('//*[@id="JoinLink"]').get_attribute("href")
    browser.get(Math_btn)
    print('Joined Maths')
def physicsJoin():
    LogIn()
    Phy_btn = browser.find_element_by_xpath('//*[@id="JoinLink"]').get_attribute("href")
    browser.get(Phy_btn)
    print('Joined Physics')
def chemJoin():
    LogIn()
    Chem_btn = browser.find_element_by_xpath('//*[@id="JoinLink"]').get_attribute("href")
    browser.get(Chem_btn)
    print('Joined Chemistry')
def doubtJoin():
    LogIn()
    DT_btn = browser.find_element_by_xpath('//*[@id="JoinLink"]').get_attribute("href")
    browser.get(DT_btn)
    print('Joined Math Doubt')

# sleep(30)
hour = (dt.datetime.now().strftime('%H:%M'))
# print(type(hour))
def checkTime():
        if hour>='8' and hour<='9:15':
            print("Maths")
            mathsJoin()
        elif hour>='9:45' and hour<='11:15':
            print("Physics")
            physicsJoin()
        elif hour>='11:30' and hour<='13':
            print("Chemistry")
            chemJoin()
            # btn2_chem = browser.find_element_by_xpath('//*[@id="JoinLink"]').get_attribute("href")
            # browser.get(btn2_chem)
        else:
            # print("Ended")
            doubtJoin()
checkTime()
    