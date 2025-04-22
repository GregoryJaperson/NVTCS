temperature = int(input("Temperature in Celcius"))
chance_of_rain = int(input("Chance of rain in percentage"))
wind_speed = int(input("Wind speed in km/h"))

if 15 <= temperature <= 25 and chance_of_rain < 40 and wind_speed < 20:
    print("Go for a hike")
elif 10 <= temperature <= 30 and chance_of_rain < 50 and wind_speed < 25:
    print("Go cycling")
elif chance_of_rain > 70 and wind_speed > 30:
    print("Stay indoors")
elif 5 <= temperature <= 20 and wind_speed < 20:
    print("Go Jogging")
else:
    print("Figure it out yourself")