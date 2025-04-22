import time

color = input("Enter a traffic light color: (RED, YELLOW, GREEN)")
color = color.upper()
while True:
    if color == "RED":
        print("Red, stop")
        time.sleep(1)
        color = "GREEN"
    elif color == "YELLOW":
        print("Yellow, get ready to stop")
        time.sleep(1)
        color = "RED"
    elif color == "GREEN":
        print("Green, go")
        time.sleep(1)
        color = "YELLOW"
    else:
        print("Invalid user input")

