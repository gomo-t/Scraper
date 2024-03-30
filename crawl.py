from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from csvCleaner import cleaner as cl
import time
import csv



def SearchDate(search_date ):
    
    # Path to the GeckoDriver (Firefox WebDriver) executable
    geckodriver_path = r'C:\\Users\\Tendekayi Gomo\\OneDrive\\Pulpit\\Trading Project\\Scraper\\geckodriver.exe'

    # Path to the Firefox binary (replace this with your actual Firefox binary path)
    firefox_binary_path = r'C:\\Program Files\\Mozilla Firefox\\firefox.exe'

    # Create a FirefoxOptions instance
    firefox_options = Options()

    # Set Firefox to run in headless mode
    firefox_options.add_argument('--headless')

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
    date_search2.send_keys(search_date)

    #Extra step to exit search box

    #Iniatiate search query
    exit_away_search= wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="default_view_1"]')))
    exit_away_search.click()

    #Iniatiate search query
    apply_search= wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[1]/section[2]/div[3]/div/div/div/div/div[2]/div[1]/div/table/tbody/tr/td[2]/input[1]')))
    apply_search.click()

    #Check for Day of the week  
    day_of_week = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[1]/section[2]/div[3]/div/div/div/div/table/tbody/tr[2]/td[1]/span')))

    # Get the text of the element
    date_of_week_text = day_of_week.text.split()
    day_of_week_text = date_of_week_text[0]
    #print("Text of the element:", day_of_week_text)

    if(day_of_week_text !='Sun' and day_of_week_text !=  'Sat'):
        #retrive information from the table
        rows = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'calendar__row--grey')))


        # Define CSV file path and open it for writing
        csv_file_path = 'calendar_data.csv'
        with open(csv_file_path, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Time', 'Event Title', 'Impact'])  # Write header row

            # Iterate through each row and extract the desired information
            for row in rows:
                try:
                    time_element = row.find_element(By.CLASS_NAME, 'calendar__time').text
                    event_title_element = row.find_element(By.CLASS_NAME, 'calendar__event-title').text
                    impact_element = row.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/section[2]/div[3]/div/div/div/div/table/tbody/tr[3]/td[3]/span').get_attribute('title')
                    writer.writerow([time_element, event_title_element, impact_element])  # Write row to CSV
                except Exception as e:
                         print(f"Error extracting data from row: {e}")
        cl(csv_file_path)


        #Representation of the event data
        #print(f"Time: {time_element}\tEvent Title: {event_title_element}\tImpact: {impact_element}\n")

        time.sleep(10)

        # Don't forget to quit the driver and stop the service when done
        driver.quit()
        service.stop()


        #exit signal
        print('Done!')

    else:
        time.sleep(10)
        print('Weekend\nDone!')
        driver.quit()
        service.stop()
        exit()

#Earliest date is 1 Jan 2007
#Input for DD-MM-YYYY format
#search_date =input('Enter search date: DD MM YYYY: ')

#function call
#SearchDate(search_date)