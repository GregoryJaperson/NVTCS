ex_list = [0, 1, 2, 3, 4] #Normal Array
ex_tuple = (0, 1, 2, 3, 4) #non-mutable
ex_set = {0, 1, 2, 3, 4} #Non-duplicate, un-ordered
ex_dict = {'a':0, 'b':1, 'c':2, 'd':3} #Relation between keys and values, mutable value

for key, value in ex_dict.items():
    print(key + ' ' +str(value))

friends_heights = []
family_heights = []
friends_count = int(input("Amount of friends"))
family_count = int(input("Amount of family"))

for i in range(friends_count):
    friends_heights.append(int(input("Enter friend's height: ")))
for i in range(family_count):
    family_heights.append(int(input("Enter family's height:")))

friends_set = set(friends_heights)
family_set = set(family_heights)
combined_set = friends_set.union(family_set)

print(friends_set, family_set, combined_set)
list_dict = []
rep = 1
while rep == 1:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    city = input("Enter your city name: ")
    list_dict.append({'name':name, 'age':age, 'city':city})
    rep = int(input("If you want to add another info type 1, otherwise 0: "))
print(list_dict)
