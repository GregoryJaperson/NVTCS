import time


seconds = int(input("Insert amount of seconds"))
for i in range(seconds, -1, -1):
    time.sleep(1)
    print(i)
print("DONE")


number = int(input("Insert a number"))
number = (number // 2)*2
for i in range(number, -1, -2):
    print(i)