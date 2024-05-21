#!/usr/bin/env python3

import pyfiglet

# Text to be displayed in the banner
text = "Project\nEuler # 19"
addText = "By: Jim Harris\nDate: 29FEB2024\n\nProblem: How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?\n"

# Specify the font ("slant" in this case)
font = "slant"

# Create the banner using pyfiglet
banner = pyfiglet.figlet_format(text, font=font, justify="left")

# Print the banner and additional text
print(banner + addText)

# Define the number of days in each month for non-leap years
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Define the number of days in each month for leap years
days_in_month_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Define the names of the months
month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# Define the names of the days of the week
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Initialize the total number of days in a year
total_days = sum(days_in_month)
# Initialize the starting day (Monday is 0, Tuesday is 1, etc.)
start_day_index = 2
# Initialize the count of Sundays on the first of the month
sundays_count = 0

# Iterate over each year in the twentieth century (1901 to 2000)
for year in range(1901, 2001):
    month_index = 0
    # Determine whether the current year is a leap year
    if year % 4 == 0:
        days_to_use = days_in_month_leap
    else:
        days_to_use = days_in_month
    # Iterate over each month in the year
    for days_in_current_month in days_to_use:
        # Iterate over each day in the month
        for day in range(1, days_in_current_month + 1):
            # Check if the current day is a Sunday and the first day of the month
            if start_day_index == 6 and day == 1:
                sundays_count += 1
            # Uncomment the following line to print the details of the current day
            # print(f"{year}: {month_names[month_index]} {day} {week_days[start_day_index]} {start_day_index}")
            # Increment the start day index
            start_day_index = (start_day_index + 1) % 7
        # Increment the month index
        month_index += 1

# Print the final count of Sundays falling on the first of the month
print("Total Sundays falling on the first of the month: " + str(sundays_count), "\n")
