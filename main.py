import os
import csv
from datetime import datetime, timedelta

def load_csv_files(data_directory):
    #load all csv files into a data array

    data = []
    for filename in os.listdir(data_directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(data_directory, filename)
            try:
                with open(file_path, 'r') as file:
                    reader = csv.reader(file)
                    next(reader)
                    for row in reader:
                        if row:  #ensure that the rows are formatted correctly
                            timestamp = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f')
                            price = float(row[1]) if row[1] else None
                            size = int(row[2]) if row[2] else 0
                            data.append((timestamp, price, size))
            except Exception as e:
                print(f"couldnt read {file_path}: {e}")
    return data

def clean_data(data):
    """Clean the data based on specified conditions."""
    cleaned_data = []
    for timestamp, price, size in data:
        # Check if the row meets the cleaning criteria (price < 400, size > 995, and in between trading hours)
        if price is None or price < 400 or size > 995 or timestamp.time() < datetime.strptime("09:30", "%H:%M").time() or timestamp.time() > datetime.strptime("16:00", "%H:%M").time():
            continue
        
        cleaned_data.append((timestamp, price, size))
    
    return cleaned_data

def parse_time_interval(interval):
    """Parse the time interval string into a timedelta object."""
    time_units = {'d': 'days', 'h': 'hours', 'm': 'minutes', 's': 'seconds'}
    total_seconds = 0
    current_number = ''
    
    #checks for each character in the interval string
    for char in interval:
        #if its a digit it will add it to the tracker current_number
        if char.isdigit():
            current_number += char
        # if the char has a letter at the end, it will covert the current number into seconds     
        elif char in time_units:
            if current_number:
                total_seconds += int(current_number) * (1 if time_units[char] == 'seconds' else
                                                         60 if time_units[char] == 'minutes' else
                                                         3600 if time_units[char] == 'hours' else
                                                         86400)  # days
                current_number = ''
    if current_number:  # handles any trailing number
        total_seconds += int(current_number)
    
    return timedelta(seconds=total_seconds)

def generate_ohlcv(data, start_time, end_time, interval):
    """Generate OHLCV data for the specified time range and interval."""
    interval_timedelta = parse_time_interval(interval)
    ohlcv_data = []
    
    current_time = start_time
    while current_time < end_time:
        #calculates the interval data to be added to current_time after OHLCV calculation
        interval_data = [d for d in data if current_time <= d[0] < current_time + interval_timedelta]
        
        #caluclates the OHLCV from the given time to start time 
        if interval_data:
            open_price = interval_data[0][1]
            high_price = max(d[1] for d in interval_data if d[1] is not None)
            low_price = min(d[1] for d in interval_data if d[1] is not None)
            close_price = interval_data[-1][1]
            volume = sum(d[2] for d in interval_data)
            #appends the data to OHLCV data
            ohlcv_data.append((current_time, open_price, high_price, low_price, close_price, volume))
        
        current_time += interval_timedelta
    
    return ohlcv_data

def save_to_csv(ohlcv_data, output_file):
    """Save the OHLCV data to a CSV file."""
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume'])
        for row in ohlcv_data:
            writer.writerow(row)


if __name__ == "__main__":
    data_directory = 'data'  
    output_file = 'ohlcv_output.csv'
    data = load_csv_files(data_directory)
    cleaned_data = clean_data(data)
    
    # define time range and interval
    start_time = datetime(2024, 9, 16, 9, 30)  # year, month, date, hour, min
    end_time = datetime(2024, 9, 16, 16, 0)  # year, month, date, hour, min
    interval = '1h'  # enter interval
    
    # generate OHLCV data
    ohlcv_data = generate_ohlcv(cleaned_data, start_time, end_time, interval)
    
    # save to CSV format
    save_to_csv(ohlcv_data, output_file)
    print(f"OHLCV data saved to {output_file}")
