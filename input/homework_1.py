#1) Write a program to check whether a number is positive, negative, or zero.
"""

get_number=int(input("Enter number:"))
if get_number>=1:
    print("number is positive")
elif get_number<0:
    print("number is negative")
else:
    print("number is zero")

"""

#2) Write a program to check whether a student passed or failed.
"""
student=input("Enter Student name:")
marks=int(input("Enter Marks:"))
if marks>=45:
    print(student + "mark is ",marks ,"which is pass")
else:
    print(student + "mark is ",marks ,"which is fail")
"""

#3) Write a program to print numbers from 1 to 100 using a for loop.
"""
for i in range(1,101):
    print(i)
"""

#4) Write a program to print numbers from 100 to 1 using a while loop.
"""
i=100
while i>=1:
    print(i)
    i -=1
"""
#5) Write a program to calculate the sum of numbers from 1 to 100.
"""
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
ans=num1+num2
print(ans)
"""
#6) Write a program to find whether a given student exists in a list.
"""
Students=["Palani","Seetha","Varnikhaa","Adwaidan"]
Student_name=input("Enter Student name:")
for name in Students:
    if Student_name==name:
          print("Name found in the list!")
          break
    else:
          print("Name not found in the list!")
"""
#7) Write a menu-driven calculator using match-case.
"""
print("even numbers only")
for num in range(1,51):
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")

result=int(input("Enter a number:"))# this get the choices number
get_input1 = int(input("Enter number:"))
get_input2 = int(input("Enter second number:"))

match result:
    case 1:
        result =get_input1+get_input2
        print(result)
    case 2:
        result =get_input1-get_input2
        print(result)
    case 3:
        result =get_input1*get_input2
        print(result)
    case 4:
        result =get_input1/get_input2
        print(result)
"""
#8) Write a program to print all even numbers from 1 to 50.
"""
print("even numbers only")
for num in range(1,51):
    if num%2==0:
        print(num)
"""


#9) Write a program to skip numbers divisible by 3 using continue.
"""
number=[1,2,3,4,5,6,7,8,9,10]
for num in number:
    if num%3==0:
        continue
    print(num)
"""

#10) Write a program to stop searching when a particular product is found using break
"""
product=["Shirt","Pants","Top","Jacket"]
get_product="Pants"
for lis in product:
    if lis==get_product:
     break
    print("product found" ,get_product)

else:
    print("product not found in the list")
"""

