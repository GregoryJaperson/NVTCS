#Celcius
temp1 = 20
temp2 = 30
temp3 = 15

#Convert to F tempnF and print C*9/5+32
def convert(temp):
    return temp*(9/5)+32
temp1F = convert(temp1)
temp2F = convert(temp2)
temp3F = convert(temp3)

print(str(temp1) + ' ' + str(temp1F))
print(str(temp2) + ' ' + str(temp2F))
print(str(temp3) + ' ' + str(temp3F))

#Determine the hottest and coldest and print
max_temp = temp1F
lowest_temp = temp1F
if max_temp < temp2F:
    max_temp = temp2F
elif max_temp < temp3F:
    max_temp = temp3F

if lowest_temp > temp2F:
    lowest_temp = temp2F
elif lowest_temp > temp3F:
    lowest_temp = temp3F
#Difference between hottest and coldest is
print("The difference between the hottest and coldest temperature is " + str(max_temp-lowest_temp) + " Fahrenheit")