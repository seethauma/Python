
"""
a=int(input("Enter a number"))
b=int(input("Enter another number"))


print(a+b)
"""
import sys

#if arg
if len(sys.argv) == 2:

    print("usage: python")
    sys.exit()

#delimiter is " " space between each arg
full_name = " ".join(sys.argv[1:]) #to pass any number of arg
#full_name = sys.argv[1] # passing only one arg
last_name = sys.argv[2]
email = full_name.lower().replace(" ",".") + last_name + "@company.com"

print(full_name,"Profile details")
print(full_name)
print(last_name)
print(email)




