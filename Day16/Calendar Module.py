import calendar
from datetime import datetime

# Input date in MM DD YYYY format
date_input = input().strip()
month, day, year = map(int, date_input.split())

# Create a date object
date_obj = datetime(year, month, day)

# Get the day of the week
day_of_week = calendar.day_name[date_obj.weekday()]

# Output the day in uppercase
print(day_of_week.upper())
