from datetime import datetime, timedelta
from crawl import SearchDate as sd

# Define your date 
query_date = datetime(2024, 3, 1)  # Change this to your desired start date

# Define the date format string expected by the input field
date_format = "%d/%m/%Y"

#Search query
search_date = query_date.strftime(date_format)
sd(search_date)  
