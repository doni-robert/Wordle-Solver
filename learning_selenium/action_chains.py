from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException


# Instantiate the Chrome webdriver with the specified options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Navigate
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Wait for everything to load
driver.implicitly_wait(10)

# Get necessary elements
language = driver.find_element(By.ID, "langSelect-EN")
language.click()

cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
products = [driver.find_element(By.ID, f"product{i}") for i in range(1, -1, -1)]

# Action chain setup
actions = ActionChains(driver)

for i in range(500):
    actions.click(cookie).perform()
    count = int(cookie_count.text.split(" ")[0])
    for product in products:
        try:
            value = int(product.text.split("\n")[1].replace(",", ""))
            if value <= count:
                upgrade_actions = ActionChains(driver)
                upgrade_actions.move_to_element(product)
                upgrade_actions.click()
                upgrade_actions.perform()
                # Update cookie count after purchasing product
                count -= value
                # Wait for cookie count to update
                driver.implicitly_wait(2)
        except StaleElementReferenceException:
            # If the element is stale, re-find it
            products = [driver.find_element(By.ID, f"product{i}") for i in range(1, -1, -1)]
            continue
    