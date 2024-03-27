from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

import time

# Path to the GeckoDriver (Firefox WebDriver) executable
geckodriver_path = r'C:\\Users\\Tendekayi Gomo\\OneDrive\\Pulpit\\Trading Project\\Scraper\\geckodriver.exe'

# Path to the Firefox binary (replace this with your actual Firefox binary path)
firefox_binary_path = r'C:\\Program Files\\Mozilla Firefox\\firefox.exe'

# Create a FirefoxOptions instance
firefox_options = Options()
firefox_options.binary_location = firefox_binary_path

# Create a service object
service = Service(geckodriver_path)

# Start the WebDriver service
service.start()

# Create a Firefox WebDriver instance with specified options
driver = webdriver.Firefox(service=service, options=firefox_options)

# Now you can use 'driver' to interact with the browser
driver.get('https://www.metalsmine.com/calendar')
print(driver.title)

time.sleep(60)

# Don't forget to quit the driver and stop the service when done
driver.quit()
service.stop()
