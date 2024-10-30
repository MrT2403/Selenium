import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.neuralnine.com/")
driver.maximize_window()

links = driver.find_elements("xpath", "//a[@href]")
for link in links:
    if "Books" in link.get_attribute("innerHTML"):
        link.click()
        break
    
# Locate the book links using the corrected XPath
book_links = driver.find_elements("xpath", "//div[contains(@class, 'elementor-column-wrap')][.//h2[text()[contains(., '7 IN 1')]]][count(.//a)=2]//a")

# Print the href attributes of the found links
for book_link in book_links:
    print(book_link.get_attribute("href"))

# Wait until the first book link is clickable
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'elementor-column-wrap')][.//h2[text()[contains(., '7 IN 1')]]][count(.//a)=2]//a[1]")))

# Click on the first book link
book_links[0].click()

# Switch to the new window
driver.switch_to.window(driver.window_handles[1])

time.sleep(3)

# Locate price buttons
buttons = driver.find_elements("xpath", "//a[.//span[text()[contains(., 'Paperback')]]]//span[text()[contains(., '$')]]")

for button in buttons:
    print(button.get_attribute("innerHTML"))

# Close the driver
driver.quit()
