from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the Google homepage
driver.get("https://www.google.com")

# Find the search box element and enter the search query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python Selenium")

# Submit the search query
search_box.send_keys(Keys.RETURN)

# Wait for the search results page to load
wait = WebDriverWait(driver, 10)
results = wait.until(EC.presence_of_element_located((By.ID, "search")))

# Perform further actions on the search results page
# ...

# The browser will remain open after the script execution