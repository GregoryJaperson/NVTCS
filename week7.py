import math

print(math.pi*(10**2))

def validate_bsn():
    bsn = input("Insert your BSN: ")

    #Counts the length of BSN
    if len(bsn) != 9:
        return False

    #Add the sum of every digit multiplied by 9 to 1
    counter = 9
    digit_sum = 0
    for digit in bsn:
        digit_sum += int(digit) * counter
        counter -= 1

    #If digit is divisible by 11, then return True
    if digit_sum % 11 == 0:
        return True
    else:
        return False

print("Your BSN is: ", validate_bsn())

def default_value(a=1 , b=2, c=3):
    return a+b+c

print(default_value(10))

def summing_up(a, b, c):
    return a+b+c
def power(integer):
    return integer**2
print(power(summing_up(2, 3, 4)))

num_list = [1,2,3,4,67,45,23,22]
def odd_even(number_list):
    odd = []
    even = []
    for number in number_list:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    return odd, even

print(odd_even(num_list))