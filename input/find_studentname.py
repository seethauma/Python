"""""
Students=["Palani","Seetha","Varnikhaa","Adwaidan"]
Student_name=input("Enter Student name:")
for name in Students:
    if Student_name==name:
          print("Name found in the list!")
          break

    else:
          print("Name not found in the list!")
  """

"""
student=input("Enter Student name:")
marks=int(input("Enter Marks:"))
if marks>=45:
    print(student + "mark is ",marks ,"which is pass")
else:
    print(student + "mark is ",marks ,"which is fail")
   
"""
"""
get_number = int(input("Enter number:"))
if get_number >= 1:
    print("number is positive")
elif get_number < 0:
    print("number is negative")
else:
    print("number is zero")
"""


num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
ans=num1+num2
print(ans)