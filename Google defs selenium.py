from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Selenium Set up
path = "D:\\Scripts\\.Dev\\Python\\.Projects\\Selenium\\chromedriver.exe"
driver = webdriver.Chrome(path)

# Defining list of words
words = [""]

# Searching and printing algo
for x in range(len(words)-1):
    driver.get("https://www.google.com/search?q=" + words[x])
    time.sleep(0.2)
    driver.execute_script('''window.open("http://google.com","_blank");''')
    time.sleep(0.2)
    driver.switch_to.window(driver.window_handles[x + 1])
    time.sleep(0.2)