from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from time import sleep


from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open the URL
driver.get("https://www.saucedemo.com")

# Display cookies before login
print("Cookies before login:", driver.get_cookies())

# Perform login
username_input = driver.find_element(by =By.ID, value="user-name").send_keys("standard_user")
sleep(2)
password_input = driver.find_element(by =By.ID, value="password").send_keys("secret_sauce")
sleep(2)
login_button = driver.find_element(by = By.ID, value="login-button").click()
sleep(2)



# Display cookies after login
print("Cookies after login:", driver.get_cookies())
sleep(5)
buger_button = driver.find_element(by = By.ID, value="react-burger-menu-btn").click()
sleep(5)


# Perform logout
logout_button = driver.find_element(by=By.ID,value="logout_sidebar_link").click()


# Close the browser
driver.quit()
