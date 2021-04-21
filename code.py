from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome("chromedriver.exe")
url = "https://www.instagram.com/?hl=en"
driver.get(url)
sleep(5)


username = driver.find_element_by_name('username')
username.send_keys('illus_by_me')
password = driver.find_element_by_name('password')
password.send_keys('himanshi')
button_login = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button > div')
button_login.click()
sleep(5)

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

sleep(1)
usernameofperson="thedivakitchen_" 
driver.get('https://www.instagram.com/' + usernameofperson)
sleep(5)
first_thumbnail = driver.find_element_by_class_name('eLAPa')
first_thumbnail.click()
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

