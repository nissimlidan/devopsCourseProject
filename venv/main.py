#LIDAN NISSIM, COURSE 1005
#ASSIGNMENT LESSSON 1 (ADVANCED)- 16/05/23
#(1) Write a python program to swap two numbers using a third variable
def swap(a,b):
    # a = 7 b = 9
    c = a # c = 7
    a = b # a = 9
    b = c # b = 7
    return a,b

first = 2
second = 5
print("#1 - swap")
print(f"Before swap - first = {first} and second = {second}")
first, second = swap(first,second)
print(f"After swap - first = {first} and second = {second}")

#(2) Write a python program to swap two numbers without using third variable
def swap2(a,b):
    return b,a

first = 16
second = 8
print("#2 - swap witout extra var")
print(f"Before swap(witout third number) - first = {first} and second = {second}")
first, second = swap(first,second)
print(f"After swap(witout third number) - first = {first} and second = {second}")

#(3) Write a python program to read two numbers and find the sum of their cubes
def sum():
    print("#3 - sum of two numbers")
    first_num = input('Choose first number')
    second_num = input('Choose second number')
    sum = int(first_num)+ int(second_num)
    print(f"The sum of {first_num} and {second_num} is {sum}")
    return sum

sum = sum()

#(4) Write a python program to read three numbers and if any two variables are equal , print that number
def number_is_equel():
    print("#4 - if number is equel")
    first_num = input('Choose first number')
    second_num = input('Choose second number')
    third_num = input('Choose third number')
    if first_num == second_num or first_num == third_num:
        print(f"{first_num} is equal to another number")
        return first_num
    elif second_num == third_num:
        print(f"{second_num} is equal to another number ")
        return second_num
    else:
        print('There is no equal numbers')

number_is_equel()

#(5) Write a python program to read three numbers and find the smallest among them
def smallest_num():
    print("#5 - smallest_number")
    first_num = input('Choose first number')
    second_num = input('Choose second number')
    third_num = input('Choose third number')

    smallest = min(first_num, second_num,  third_num)
    print(f"The smallest num is {smallest}")

smallest_num()
