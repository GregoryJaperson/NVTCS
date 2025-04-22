number = 90
row = 0

for i in range(10, number+1, 1):
    row += 1
    if i%5 == 0 and i%3 == 0:
        print("!!", end="  ")
    elif i%7 == 0:
        print(str(i)[1:2], end="  ")
    else:
        print(i, end="  ")
    if row == 9:
        print()
        row = 0
