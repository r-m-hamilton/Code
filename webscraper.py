# 1/30/2021
# Web Scraper - scan web pages for a specific element, returning 
# information in a CSV file
# Added to github 2/15/2021

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/usr/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

# Web driver waits 10 seconds until it locates the element with ID "main"
# if it doesn't work it quits
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    # Finds all elements inside of main with an article tag, loops through those 
    # elements and prints the ones with an entry-summary class name
    articles = main.find_elements_by_tag_name("article") 
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)
finally:
    driver.quit()


