""""
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")

result=int(input("Enter a number:"))
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
print("even numbers only")
for num in range(1,51):
    if num%2==0:
        print(num)