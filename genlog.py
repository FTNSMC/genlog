import csv
import socket
import time

def read_logs(file_path):
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
                time.sleep(0.001) #increase to slow log send rate, reduce to increase
            s.close()
        except Exception as e:
            print("Error sending log entry to {}:{}: {}".format(server_address, server_port, e))

def main():
    log_file_path = "/opt/genlog/logsample/sample.csv"
    destinations = [
        ("<IP>", 514),  # First destination IP and port
        #("<IP>", 514),  # Second destination IP and port
        # Add more destinations as needed
    ]

    while True:
        log_entries = [process_log_entry(entry) for entry in read_logs(log_file_path)]
        forward_log_entries(log_entries, destinations)
        time.sleep(5)  # Delay before re-reading the file

if __name__ == "__main__":
    main()
