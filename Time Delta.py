from datetime import datetime
t = int(input())
for i in range(0,t):
# Parse the timestamps into datetime objects
    date1 = input()
    date2 = input()
    timestamp1 = datetime.strptime(date1, "%a %d %b %Y %H:%M:%S %z")
    timestamp2 = datetime.strptime(date2, "%a %d %b %Y %H:%M:%S %z")
    # Calculate the difference between the timestamps
    difference = timestamp1 - timestamp2
    # Extract the difference in seconds
    difference_in_seconds = abs(difference.total_seconds())

    print(int(difference_in_seconds))
