#Average of numbers in the list
a = [1,2,3,4,5,6,7,8,9,10]
b = 0
for i in a:
    b = b+i

print(f' Average of numbers in the list: {b/len(a)}')


#Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable

a = int(input("Enter the first input: "))
b = int(input ("Enter the Second input: "))

c = a+b
a = c-a
b = c-b

print(f'Value of a: {a}')
print(f'Value of b: {b}')

#Python Program to Check Whether a Number is Positive or Negative
a = int(input("Enter any number: "))
if a>0:
    print("The number is positive")
if a<0:
    print("The number is negative")

#Python Program to Take in the Marks of 5 Subjects and Display the Grade
a = int(input("Enter your subject1 mark: "))
b = int(input("Enter your subject2 mark: "))
c = int(input("Enter your subject3 mark: "))
d = int(input("Enter your subject4 mark: "))
e = int(input("Enter your subject5 mark: "))

n = int(input("Enter number of subjects: "))

total = a+b+c+d+e
if total>500:
        print("You have entered wrong details")
avg = total/n
if avg < 50:
        print ("You got E grade")
elif (avg >=50 and avg<60):
        print("You got D grade")
elif (avg >=60 and avg<70):
        print("You got C grade")
elif (avg >=70 and avg<80):
        print("You got B grade")
elif (avg >=80 and avg<90):
        print("You got A grade")
elif avg >=90:
        print("You got A+ grade")

#Python Program to Print all Numbers in a Range Divisible by a Given Number

a = int(input("Enter any number to divide: "))
list = []
for i in range(1,100):
    if i%a ==0:
        list.append(i)
for j in list:
    print(j)

# Python Program to Read Two Numbers and Print Their Quotient and Remainder

a = int(input("Enter numerator number: "))
b = int(input("Enter denominator number: "))

quotient = a//b
remainder = a%b

print("Quotient is: ",quotient)
print("Remainder is: ",remainder)


#Python Program to Accept Three different Digits and Print all Possible Combinations from the Digits
a = int(input("Enter first number: "))
b = int(input("Enter Second number: "))
c = int(input("Enter third number: "))
d = []
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])


#Python Program to Print Odd Numbers Within a Given Range

a = int(input("Enter the range of numbers: "))

for i in range(1,a+1):
    if (i%2!=0):
        print(i)

#Python Program to Find the Sum of Digits in a Number
a = int(input("Enter any number: "))
list = []
while(a>0):
    last_number = a%10
    list.append(last_number)
    a = a//10

result = 0
for i in list:
    result = result+i

print(result)

#Python Program to Find the Smallest Divisor of an Integer

a = int(input("Enter any number: "))

for i in range(2,a+1):
    if a%i == 0:
        print("The smallest divisible number is: ",i)
    break

#Python Program to Count the Number of Digits in a Number

a = int(input("Enter any number: "))
i = 0
while(a>0):
    a = a//10
    i = i+1
print("The number of digits: ",i)

#Python Program to Check if a Number or string is a Palindrome

a = input("Enter any number or string: ")
d = []
for j in a:
    d.append(j)
b = []
c = len(a)
print("The value of c is: ",c)
while(c>0):
    for i in a[c-1]:
        b.append(i)
    c = c-1
if b == d:
    print("This number is palindrome")

#Python Program to Print all Integers that Aren't Divisible by Either 2 or 3 and Lie between 1 and 50.

for i in range(0,51):
    if(i%2!=0&i%3!=0):
        print(i)



else:
    print("This is not a palindrome")


#Python Program to Check if a Date is Valid and Print the Incremented Date if it is

date = input('Enter any date in dd/mm/yyyy format: ')
dd,mm,yy = date.split("/")
dd = int(dd)
mm = int(mm)
yy = int(yy)

if(mm==1 or mm ==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
    maximum1 =31
elif(mm==4 or mm==6 or mm==9 or mm==11):
    maximum1 = 30
elif(yy%4 ==0 and yy%100 != 0 or yy%400 ==0):
    maximum1 = 29
else:
    maximum1 = 28

if(mm<1 or mm>12):
    print("The entered month is invalid")
elif(dd<1 or dd>maximum1):
    print("The entered date is invalid")
elif(dd == maximum1 and mm!=12):
    dd = 1
    mm = mm+1
    print("The incremented/next date is: ",dd,mm,yy)
elif(dd == maximum1 and mm==12):
    dd = 1
    mm = 1
    yy = yy+1
    print("The incremented/next date is: ",dd,mm,yy)
    print("And Python wishing you a great new year ahead")
else:
    dd = dd+1
    print("The incremented/next date is: ",dd,mm,yy)

#Python Program to Compute Simple Interest Given all the Required Values

p = int(input("Enter the principle amount: "))
r = int(input("Enter the rate of interest: "))
n = int(input("Enter the number of terms: "))

simple_interest = p*r*n

print("Simple interest is: ",simple_interest)

#Python Program to Check Whether a Given Year is a Leap Year

year = int(input("Enter the year: "))

if(year%4 == 0 and year%100 !=0 or year%400 ==0):
    print("The given number is leap year")
else:
    print("The given number is not a leap year")

#Python Program to Read Height in Centimeters and then Convert the Height to Feet and Inches

height = int(input("Enter your height input in centimeters: "))

foot = (height*0.0328)
inches = (height*0.394)

print(f'The given height is {foot} foot and {round(inches,2)} inches')


#Python Program to Take the Temperature in Celcius and Covert it to Farenheit

celcius = int(input("Enter the celcius value: "))

fahrenheit = (celcius * 1.8) + 32

print("The fahrenheit value for the given celcius value is",fahrenheit)

#Python Program to Compute Prime Factors of an Integer

a = int(input("Enter any number: "))
b = []
for i in range(2,a):
    if a%i == 0:
        b.append(i)
c = b.sort()
d = c[0]
print("The smallest prime factor of the number is: ",d)

#Python Program to Generate all the Divisors of an Integer

a = int(input("Enter any digit: "))
print("The given number is divisible by: ")
for i in range(1,a):
    if a%i == 0:
        print(i)

#Python Program to Print Table of a Given Number

a = int(input("Enter a number: "))
print("The table of the given number till 100 is: ")
for i in range(1,101):
    print(i, "*" ,a, "=" ,i*a)


#Python Program to Print Sum of Negative Numbers, Positive Even Numbers and Positive Odd numbers in a List

a = int(input("Enter the number of elements you want in the list: "))
list = []

for i in range(0,a):
    b = int(input("Enter the element number: "))
    list.append(b)

negative_numbers = []
positive_odd = []
positive_even = []

categories = [negative_numbers,positive_odd,positive_even]

for i in list:
    if(i<0):
        negative_numbers.append(i)
for j in list:
    if(j>0 and j%2 == 0):
        positive_even.append(j)
for k in list:
    if(k>0 and k%2 != 0):
        positive_odd.append(k)
starter = 0
for cat in categories:
    for m in cat:
        m = m+starter
        starter = m
    print("The sum of",cat,"in list is",starter)


#Python Program to Print Largest Even and Largest Odd Number in a List

a = int(input("Enter the number of the elements you want in the list: "))
list = []
for i in range(0,a):
    b = int(input("Enter the input: "))
    list.append(b)
list.sort(reverse = True)
print("The largest number in the list is: ",list[0])
print("The smallest number in the list is: ",list[-1])

#Python Program to Find Those Numbers which are Divisible by 7 and Multiple of 5 in a Given Range of Numbers

a = int(input("Enter the number range: "))
print("The below number/numbers is/are divisible by 7 and multiple by 5")
for i in range(1,a+1):
    if (i%7==0 and i%5 == 0):
        print(i)

#Python Program to Check if a Number is an Armstrong Number

a = int(input("Enter the number: "))
temp = a
list = []
while temp>0:
    b = temp%10
    list.append(b)
    c = temp//10
    temp = c
d = len(list)
result = 0
for i in list:
    result = result + i**d
if result == a:
    print("The entered number is Amstrong number")
else:
    print("The entered number is not a Amstrong number")

#Python Program to Print the  right angle triangle for n number of rows given by the user

a = int(input("Enter a number of rows: "))
list = []
for i in range(1,a+1):
    list.append(i)
l = len(list)
for i in list:
     print(" "*(l-i),end=" ",sep=" ")
     print("*"*i)

#Program to check Strong Number

a = int(input("Enter the number: "))
temp = a
list = []
while(temp>0):
    last_digit = temp%10
    list.append(last_digit)
    temp = temp//10
len = len(list)
sum_list = []
for i in list:
    if i == 1:
        sum_list.append(1)
    else:
        for j in range(1,i):
            sum = i*j
            i = sum
        sum_list.append(sum)
starter = 0
for k in sum_list:
    result = starter + k
    starter = result
if(starter == a):
    print("The entered number is a strong number")
else:
    print("The entered number is not a strong number")

#Python Program to Find the LCM of Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a>b:
    max = a
else:
    max = b
while(1):
    if(max%a == 0 and max%b == 0):
        print("LCM is: ",max)
        break
    max = max+1

#Python Program to Check If Two Numbers are Amicable Numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
list = []
if a>b:
    max = a
    min = b
else:
    max = b
    min = a
for i in range(1,max):
    if (max%i == 0):
        list.append(i)
starter = 0
for result in list:
    result = result +starter
    starter = result
if (result == min):
    print("The entered number are amicabe numbers")
else:
    print("The entered numbers are not amicable numbers")

#Python Program to Find the Area of a Triangle Given All Three Sides
import math
a = int(input("Enter the first side of the triangle: "))
b = int(input("Enter the second side of the triangle: "))
c = int(input("Enter the third side of the triangle: "))

perimeter = (a+b+c)/2

area = math.sqrt(perimeter*(perimeter-a)*(perimeter-b)*(perimeter-c))

print("The area of the triangle for the given sides is: ",area)

#Python Program to Check if a Number is a Prime Number

a = int(input("Enter a number: "))
for i in  range(2,a):
    if (a%i == 0):
        print("The given number is not a prime number")
        break
else:
    print ("The given number is a prime number")

#Python Program to Print all the Prime Numbers within a Given Range

a = int(input("Enter the range to print the prime numbers: ")) #To work

#Python Program to Print Numbers in a Range (1,upper) Without Using any Loops
def printer(upper):
    if (upper>0):
        printer(upper-1)
        print(upper)
upper = int(input("Enter the upper range: "))
printer(upper)

"""Problems based on lists"""

#Python Program to Find the Largest Number in a List.

list = []
n = int(input("Enter the number of elements in the list: "))
for i in range(1,n+1):
    a = int(input("Enter the number: "))
    list.append(a)
list.sort()
print("The largest number in the list is: ",sorted_list[n-1])

#Python Program to Find the Second Largest Number in a List

list = []
n = int(input("Enter the number of elements in the list: "))
for i in range(1,n+1):
    a = int(input("Enter the number: "))
    list.append(a)
list.sort()
print("The largest number in the list is: ",sorted_list[n-2])

#Python Program to Put Even and Odd elements in a List into Two Different Lists.

list = []
even_list = []
odd_list = []
n = int(input("Enter the number of elements in the list: "))
for i in range(1,n+1):
    a = int(input("Enter the number: "))
    list.append(a)
for i in list:
    if (i%2 == 0):
        even_list.append(i)
    if (i%2!=0):
        odd_list.append(i)

#Python Program to Merge Two Lists and Sort it

list1 = []
list2 = []
n1 = int(input("Enter the number of elements in list1"))
n2 = int(input("Enter the number of elements in list2"))

for i in range(1,n1+1):
    a = int(input("Enter the number: "))
    list1.append(a)
for j in range(1,n2+1):
    b = int(input("Enter the number: "))
    list2.append(b)
list3 = list1+list2
list3.sort()
for k in list3:
    print(k)

#Python Program to Sort the List According in the bubble sort method.

list = [54,78,65,21,23,54,25]
for i in range(0,len(list)):
    for j in range(0,(len(list)-i-1)):
        if (list[j] > list[j+1]):
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
for k in list:
    print(k)

#Python Program to Sort a List According to the Length of the Elements and print the lengthy element in the list.
 a = []
 n = int(input("Enter the number of elements: "))
 for i in range(1,n+1):
     element = int(input("Enter a string element: "))
     a.append(element)
a.sort(key = len)
print("The lenthy string in the list is: ",a[-1])

#Python Program to Find the Union of two Lists

a = [1,2,3,4,5,6]
b = [4,5,6,7,8,9]

union = list(set().union(a,b))
print(union)

#Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number

lower_range = int(input("Enter the lower range: "))
upper_range = int(input("Enter the upper range: "))

a = [(x,x**2) for x in range(lower_range,upper_range)]
print(a)

#Python Program to Swap the First and Last Value of a List.

a = [1,2,3,4,5,6,7,8,9,10]
temp = a[0]
a[0] = a[-1]
a[-1] = temp
print(a)

#Python Program to Remove the Duplicate Items from a List

a =[1,2,3,4,3,5,2,4,5,7]
b = []
for i in a:
    if i not in b:
        b.append(i)
print("The unique elements are: ")
for j in b:
    print(j)

#Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List

import random as rd
list = []
for i in range(0,20):
    n = rd.randint(1,20)
    list.append(n)
print(list)

#Python Program to Find Element Occurring Odd Number of Times in a List.

n = int(input("Enter the number of the elements you want in the list: "))
list = []
odd_list = []
for i in range(1,n+1):
    a = int(input("Enter the element: "))
    list.append(a)
for j in list:
    if j%2!=0:
        odd_list.append(j)
length = len(odd_list)
print("Number of the odd numbers in the list is",length)

#Python Program to Read a List of Words and Return the Length of the Longest One

n = int(input("Enter the number of strings you want in list: "))
list = []
list_len=[]
for i in range(0,n):
    a = input("Enter the string: ")
    list.append(a)
for j in range(0,n):
    starter = 0
    for k in list[j]:
        starter = starter+1
    list_len.append(starter)
list_len.sort()
print("The length of the longest string in the list is: ",list_len[-1])

#Python Program to Read a List of Words and Return the Longest string in the list.

n = int(input("Enter the number of strings you want in list: "))
list = []
list_len=[]
for i in range(0,n):
    a = input("Enter the string: ")
    list.append(a)
for j in range(0,n):
    starter = 0
    for k in list[j]:
        starter = starter+1
    list_len.append(starter)
index = list_len.index(max(list_len))
print("The longest word in the list is : ",list[index])

#Python Program to Read a List of Words and Return the Longest string in the list.

n = int(input("Enter the number of strings you want in list: "))
list = []
list_len=[]
for i in range(0,n):
    a = input("Enter the string: ")
    list.append(a)
for j in range(0,n):
    starter = 0
    for k in list[j]:
        starter = starter+1
    list_len.append(starter)
index = list_len.index(max(list_len))
print("The longest word in the list is : ",list[index])

#Python Program to Remove the Duplicate Items from a List

n = int(input("Enter the numbers of elements you want in list: "))
list = []
new_list = []
list_len=[]
for i in range(0,n):
    a = int(input("Enter the number: "))
    list.append(a)
for j in list:
    if j not in new_list:
        new_list.append(j)

print(new_list)
