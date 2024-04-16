# Import the necessary modules from the Selenium library
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create Chrome options with experimental option to detach
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Instantiate the Chrome webdriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to Wikipedia
driver.get("https://www.wikipedia.org/")

# Print the title of the webpage
print(driver.title)

search = driver.find_element(By.ID, "searchInput")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "mw-body-content"))
    )
    print(main.text)

finally:
    driver.quit()







# Close the webdriver
