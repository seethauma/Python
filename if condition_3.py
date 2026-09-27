"""
Multi line comment
"""
'''
This is also multiple line comment
'''
amount =1200
tax= amount * 0.18
total = amount + tax
print(total)
if total > 1000 :
    discount = total * 0.10
    total -= discount
    print(total)

###############################################3
age = 65
student = 'yes'
if age >= 60 or student == 'yes' :
    print("Yes discount")
else:
     print("Not discount")