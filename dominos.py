from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Replace these placeholders with your actual Domino's account details
username = "your_username"
password = "your_password"

# Replace with your address details
address = "sos tech services"
city = "amritsar"
state = "punjab"
zipcode = "143001"

# Replace with the details of the pizza you want to order
pizza_name = "Pepperoni Pizza"
topping1 = "Pepperoni"
topping2 = "Cheese"

# Start the browser
driver = webdriver.Chrome()

# Open Domino's website
driver.get("https://www.dominos.com/")

# Log in
login_button = driver.find_element(By.LINK_TEXT, "Log In")
login_button.click()

time.sleep(2)  # Allow time for the page to load

username_field = driver.find_element(By.ID, "Email")
password_field = driver.find_element(By.ID, "Password")

username_field.send_keys(username)
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

# Add delivery address
time.sleep(2)  # Allow time for the page to load

address_button = driver.find_element(By.XPATH, "//a[@href='#/account/address']")
address_button.click()

time.sleep(2)  # Allow time for the page to load

address_field = driver.find_element(By.ID, "Street")
city_field = driver.find_element(By.ID, "City")
state_field = driver.find_element(By.ID, "Region")
zipcode_field = driver.find_element(By.ID, "Postal_Code")

address_field.send_keys(address)
city_field.send_keys(city)
state_field.send_keys(state)
zipcode_field.send_keys(zipcode)
zipcode_field.send_keys(Keys.RETURN)

# Choose pizza and toppings
time.sleep(2)  # Allow time for the page to load

pizza_button = driver.find_element(By.XPATH, f"//a[contains(text(), '{pizza_name}')]")
pizza_button.click()

time.sleep(2)  # Allow time for the page to load

topping1_checkbox = driver.find_element(By.XPATH, f"//label[contains(text(), '{topping1}')]")
topping1_checkbox.click()

topping2_checkbox = driver.find_element(By.XPATH, f"//label[contains(text(), '{topping2}')]")
topping2_checkbox.click()

# Proceed to checkout (you may need to adapt this part based on the website's structure)
time.sleep(2)  # Allow time for the page to load

checkout_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Checkout')]")
checkout_button.click()

# Close the browser
time.sleep(5)  # Allow time for the order to be processed (adjust as needed)
driver.quit()
