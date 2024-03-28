from datetime import datetime, timedelta
from crawl import SearchDate as sd

# Define the date format string expected by the input field
date_format = "%d/%m/%Y"

# Get user input for the start date
start_date_input = input("Enter the start date (DD/MM/YYYY): ")

# Get user input for the end date
end_date_input = input("Enter the end date (DD/MM/YYYY): ")

try:
    # Parse the user inputs into datetime objects using the specified format
    start_date = datetime.strptime(start_date_input, date_format)
    end_date = datetime.strptime(end_date_input, date_format)
except ValueError:
    print("Invalid date format. Please enter dates in the format DD/MM/YYYY.")
else:
    # Loop through the date range and call the sd function for each date
    current_date = start_date
    while current_date <= end_date:
        search_date = current_date.strftime(date_format)
        sd(search_date)  # Call the sd function from the crawl module
        current_date += timedelta(days=1)  # Increment the current date by one day
