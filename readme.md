
# Automatic Internet Speed Test Application


This Python script performs automatic speed tests of your internet connection at specified intervals. It utilizes the Speedtest library to collect download, upload, and ping data, storing this information in lists along with the date and time of each test.


## How to Use

1.Ensure you have the necessary libraries installed by running pip install speedtest-cli.

2.Run the script in a Python environment.

3.Enter the desired time interval (in seconds) between each speed test when prompted.

4.The script will automatically conduct speed tests based on the specified interval.
## Functionality

- Speed Test: Measures download and upload speeds in Mbps, as well as ping in milliseconds.
- Data Storage: Results are displayed in the console and stored in lists for potential analysis.
- Automatic Testing: Tests are scheduled at regular intervals as per user input.
- Interruption: Press Ctrl + C to stop the script at any time.


## Sample Output

Welcome to the Automatic Internet Speed Test!

Enter the interval (in seconds) between each internet speed test: 60

Testing the speed...

Download Speed: 50.25 Mbps
Upload Speed: 20.45 Mbps
Ping: 25 ms
Date and Time of Test: 2021-09-01 15:30:45

Next test will be conducted in 60 seconds...


## How to Stop

- Press Ctrl + C to halt the execution of the script.
## Future Enhancements

If you wish to visualize the results graphically, consider incorporating the Matplotlib library to plot the data from the download, upload, and ping lists over time.

For further assistance or inquiries, feel free to reach out. Enjoy testing your internet speed automatically!
