# python calculator to do {add,sub,mul,div}
operator = input("Enter the operator you need to do(+,-,*,/):")

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

if operator== "+":
    result= num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator== "*":
    result= num1 * num2
    print(round(result,3))
elif operator=="/":
    result=num1 / num2
    print(round(result, 3))
else:
    print(f"the {operator} is not valid")
