n = 0
m = 0
while m >= n:
    n = int(input("Enter number N"))
    m = int(input("Enter number M, where M is smaller than N"))

counter = 0
while counter <= n:
    print(counter)
    counter = counter + m