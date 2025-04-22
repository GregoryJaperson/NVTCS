word = "albertjan"

i = 0
for letter in word:
    i+=1
print(i)

if len(word) < 2:
    print("")
else:
    print(word[0:2] + " " + word[-2:])

for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=' ')
    elif i % 3 == 0:
        print("Fizz", end=' ')
    elif i % 5 == 0:
        print("Buzz", end=' ')
    else:
        print(i, end=' ')

i = 0
while i <= 10:
    print('*' * i)
    i += 1
while i > 0:
    print('*' * i)
    i -= 1

array = []
while True:
    array.append(float(input("Insert number to insert to the array")))
    choice = int(input(("1 for inserting, 2 for searching")))
    if choice == 2:
        break
    elif choice == 1:
        continue
search = float(input("Insert number that you want to search"))
for i in range(0, len(array)):
    if array[i] == search:
        print(i)
