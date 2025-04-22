import statistics

first_name = input("Insert First Name")
last_name = input("Insert Last Name")
score_1 = int(input("Insert First Score"))
score_2 = int(input("Insert First Score"))
score_3 = int(input("Insert First Score"))
total_score = score_1+score_2+score_3

print(last_name+first_name)
print(total_score)

print(round(total_score/3, 2))

