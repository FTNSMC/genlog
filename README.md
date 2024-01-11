Setup Instructions for genlog.py
Creating Required Directories
Open a terminal.

Create the directory for genlog:
mkdir /opt/genlog/

Create a subdirectory for log samples:
mkdir /opt/genlog/logsample/

Adding the Script
Place the genlog.py script in the /opt/genlog/ directory.

Preparing Log Files
Save your CSV files with raw logs into the /opt/genlog/logsample/ directory. Ensure these files are in the correct CSV format expected by the script (standard export from FortiSIEM with only raw event log column).

Running the Script
Before running the script, edit genlog.py to set the correct destination IP addresses and any other configurations specific to your setup.

To run the script, navigate to the /opt/genlog/ directory in the terminal:
cd /opt/genlog/

Execute the script with Python:
python genlog.py

Alternatively, you can run the script directly from any location using:
python /opt/genlog/genlog.py

Note: The script is written for Python 2.7. Ensure you have Python 2.7 installed and it's the version being used to run the script.


Additional Notes
The script will continuously read and forward logs from all CSV files in the /opt/genlog/logsample/ directory.
If you encounter permission issues when running the script, you may need to grant execute permissions to the script:

chmod +x /opt/genlog/genlog.py
