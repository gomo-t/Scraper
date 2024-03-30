from datetime import datetime
from crawl import SearchDate as sd


def dayCrawl(inputDate):
    # Define the date format string expected by the input field
    date_format = "%d/%m/%Y"

    # Get user input for the search date
    user_input = inputDate#input("Enter the date of search (DD/MM/YYYY): ")

    try:
        # Parse the user input into a datetime object using the specified format
        search_date = datetime.strptime(user_input, date_format)
    except ValueError:
        print("Invalid date format. Please enter the date in the format DD/MM/YYYY.")
    else:
        # Call your search function with the formatted search date
        search_date_str = search_date.strftime(date_format)
        sd(search_date_str)

