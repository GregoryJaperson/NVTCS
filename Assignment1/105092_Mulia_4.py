import time
from datetime import datetime
# Get current Unix time
currentUnixTime = time.time()
# Input user's birth date

name = input("your name") #change with your name
day = int(input("your birth date")) # change with your birth day
month = int(input("your birth month")) # change with your birth month
year = int(input("your birth year")) # change with your year
# Convert birth date to Unix time
birthDate = datetime(year, month, day)
birthUnixTime = time.mktime(birthDate.timetuple())
# Calculate age in seconds
ageInSeconds = currentUnixTime - birthUnixTime
# Convert age from seconds to years, months, and days

print(ageInSeconds)

years = ageInSeconds // 31536000
months = (ageInSeconds % 31536000) // 2629746
days = ((ageInSeconds % 31536000) % 2629746) // 86400

print(name + " is " + str(years) + " years, " + str(months) + " months, and " + str(days) + " days old")

