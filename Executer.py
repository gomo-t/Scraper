from DayCrawl import dayCrawl as dc
from Histcrawl import historyCrawl as hc
from argparse import ArgumentParser

parser = ArgumentParser()

# Usage message for program
parser.usage = """
Use this program to perform sraping of daily and historical data from metalsmine.com/calendar

-d is for news for that day eg -d 19/03/2009
-s ,-e is when looking for historical data eg. -s 19/03/2009 e-20/03/2009

"""

#parser.add_argument("-d", "--daynews", action="store_true")
parser.add_argument("-d", "--date", type=str, help="Specify the date in DD-MM-YYYY format for Day Crawl")
parser.add_argument("-s", "--histStartDate", type=str, help="Specify the date in DD-MM-YYYY format for Histcrawl")
parser.add_argument("-e", "--histEndDate", type=str, help="Specify the date in DD-MM-YYYY format for Histcrawl")

args = parser.parse_args()

# Accessing the date argument value
if args.date:
    specified_date = args.date
    # Call the dayCrawl method with the specified date
    dc(specified_date)
    
if args.histStartDate:
    histStartSpecified_date = args.histStartDate

    histEndSpecified_date = args.histEndDate

    #call the Histcrawl method with the specified dates
    hc(histStartSpecified_date, histEndSpecified_date)
