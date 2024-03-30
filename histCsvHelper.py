import csv
from csvCleaner import cleaner as cl


def DataTransfer():
    # Source CSV file path
    source_csv_file = "C:\\Users\\Tendekayi Gomo\\OneDrive\\Pulpit\\Trading Project\\Scraper\\calendar_data.csv"

    # Destination CSV file path
    destination_csv_file = "C:\\Users\\Tendekayi Gomo\\OneDrive\\Pulpit\\Trading Project\\Scraper\\HistoryData.csv"

    # Read data from source CSV file
    with open(source_csv_file, mode='r', newline='') as source_file:
        reader = csv.reader(source_file)
        data_to_append = list(reader)

    # Append data to destination CSV file
    with open(destination_csv_file, mode='a', newline='') as destination_file:
        writer = csv.writer(destination_file)
        writer.writerows(data_to_append)
        

    print("Data copied and appended to destination CSV file successfully.")
    #cl(destination_csv_file)
