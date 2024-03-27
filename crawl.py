from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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
driver.get('https://metalsmine.com/calendar')

# Wait for the date sorter element to be clickable
wait = WebDriverWait(driver, 10)
date_search = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[1]/section[2]/div[3]/div/div/div/div/div[1]/ul/li[2]/h2/a")))
date_search.click()

#Wait and click the input field
date_search2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="calendar-date-range-1"]')))
date_search2.click()

#Enter search range for calendar

# Perform Control + A (select all)
date_search2.send_keys(Keys.CONTROL + 'a')

# Perform Backspace (delete the selected text)
date_search2.send_keys(Keys.BACKSPACE)

#Input date text for the field
date_search2.send_keys('13 Mar 2014')

#Extra step to exit search box

#Iniatiate search query
exit_away_search= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="default_view_1"]')))
exit_away_search.click()

#Iniatiate search query
apply_search= wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[1]/section[2]/div[3]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr/td[2]/input[1]')))
apply_search.click()

#retrive information from the table
rows = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'calendar__row--grey')))

# Iterate through each row and extract the desired information
for row in rows:
    time_element = row.find_element(By.CLASS_NAME, 'calendar__time').text
    event_title_element = row.find_element(By.CLASS_NAME, 'calendar__event-title').text
    impact_element = row.find_element(By.CLASS_NAME, 'calendar__impact').get_attribute('title')

#Representation of the event data
    print(f"Time: {time_element}\tEvent Title: {event_title_element}\tImpact: {impact_element}\n")
    

time.sleep(30)


# Don't forget to quit the driver and stop the service when done
driver.quit()
service.stop()
