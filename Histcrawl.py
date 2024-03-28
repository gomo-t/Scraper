from datetime import datetime, timedelta
from crawl import SearchDate as sd

# Define your date range
start_date = datetime(2024, 3, 1)  # Change this to your desired start date
end_date = datetime(2024, 3, 5)  # Change this to your desired end date

# Define the date format string expected by the input field
date_format = "%d/%m/%Y"

# Loop through the date range and call the fetch_and_retrieve_data function for each date
current_date = start_date
while current_date <= end_date:
    search_date = current_date.strftime(date_format)
    sd(search_date)  # Call the fetch_and_retrieve_data function from the crawl module
    current_date += timedelta(days=1)  # Increment the current date by one day
