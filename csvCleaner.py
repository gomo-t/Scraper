import pandas as pd

def cleaner(csv_name):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_name)

    # Forward fill the missing time values
    df['Time']=df['Time'].ffill()

    # Save the updated DataFrame to the same CSV file
    df.to_csv(csv_name, index=False)

    print('Updated CSV file saved successfully.')
