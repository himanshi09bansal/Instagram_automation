# import libraries 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
from selenium.common.exceptions import NoSuchElementException

#driver = webdriver.Chrome("chromedriver.exe")
driver = webdriver.Chrome('/Users/himanshigupta/Desktop/Python/Detection/chromedriver') 
url = "https://www.instagram.com/?hl=en"
driver.get(url)
sleep(5)

# Enter the username and password

username = driver.find_element_by_name('username')
username.send_keys('illus_by_me')
password = driver.find_element_by_name('password')
password.send_keys('himanshi')

# Code to click on login button

button_login = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button > div')
button_login.click()
sleep(5)

# try and exception cases 

try:
    notsave = driver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
    notsave.click()
    sleep(5)
except:    
    sleep(2)

try:
    notnow = driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
    notnow.click() 
    sleep(3)
except:    
    sleep(2)

# Code to type the nam of the account

sleep(1)
usernameofperson="instagram" 
driver.get('https://www.instagram.com/' + usernameofperson)
sleep(5)

# Code to follow the account

first_thumbnail = driver.find_element_by_class_name('_5f5mN')
first_thumbnail.click()

# Code to like all the posts 

second_thumbnail = driver.find_element_by_class_name('eLAPa')
second_thumbnail.click()
sleep(3)
next_post='1'
null=''
liked,unlike=0,0
while next_post is not null:
    if liked>0 or unlike>0:
        next_post.click()
        sleep(3)
    like = driver.find_element_by_xpath("//*[@aria-label='Like']")
    like.click()
    liked +=1
    sleep(3)             
    try:
        next_post = driver.find_element_by_link_text('Next')
    except :
        next_post = null
    if liked%10==0:
        print(liked)
print(str(liked)+' Posts Liked!') 

# the end
