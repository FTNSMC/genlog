import csv
import socket
import time
import glob
import os

def read_logs(directory_path):
    for file_path in glob.glob(os.path.join(directory_path, '*.csv')):
        with open(file_path, 'rb') as file:
            reader = csv.reader(file)
            for row in reader:
                yield row

def process_log_entry(log_entry):
    return ','.join(log_entry)

def forward_log_entries(log_entries, destinations):
    for server_address, server_port in destinations:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((server_address, server_port))
            for entry in log_entries:
                s.sendall(entry.encode() + '\n')
                time.sleep(0.001)  # Adjust as needed
            s.close()
        except Exception as e:
            print("Error sending log entry to {}:{}: {}".format(server_address, server_port, e))

def main():
    log_directory_path = "/opt/genlog/logsample"  # Directory path
    destinations = [
        ("<IP>", 514),  # Replace <IP> with the actual IP
        # Add more destinations as needed
    ]

    while True:
        log_entries = [process_log_entry(entry) for entry in read_logs(log_directory_path)]
        forward_log_entries(log_entries, destinations)
        time.sleep(5)  # Delay before re-reading the files

if __name__ == "__main__":
    main()
