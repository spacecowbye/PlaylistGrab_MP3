# import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import webdriver_manager.chrome

# create a new instance of the webdriver
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(executable_path=ChromeDriverManager().install()))

# navigate to the website
driver.get('https://ytmp3.nu/o5S')

# find the search bar element and send keys to it
search_bar = driver.find_element_by_name('q')
search_bar.send_keys('your search query')

# press the enter key to initiate the search
search_bar.send_keys(Keys.ENTER)

# wait for the page to load
time.sleep(5)

# close the browser
driver.quit()
