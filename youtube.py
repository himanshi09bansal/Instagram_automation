from selenium import webdriver
import time
driver = webdriver.Chrome("chromedriver.exe")
url = "https://www.youtube.com/"
driver.get(url)
 
time.sleep(1)
 
search = driver.find_element_by_name("search_query")
search.send_keys("Sahaj Oberoi")
 
time.sleep(2)  
 
driver.find_element_by_css_selector('button[aria-label="Search"]').click()
time.sleep(10)
driver.find_element_by_css_selector('yt-formatted-string[id="description"]').click()
