# conditional expression = A one line shortcut for if-else statemet (ternary operator)
#     print or assign one of two values based on a condition 
# X if condition else Y

#example 1
num=-8 

print("postive"if num>0 else "negative")
#example 2 
num =10
result = "even" if num % 2==0 else"odd"

print(result)
#example 3
num =5
a=6
b=7
age = 25
temperature =30
user_role = "admin"
max_num = a if a> b else b
min_num = a if a<b else b
status =" adult" if age>25 else "child"
weather = "hot" if temperature>30 else "cold"
access_level = "full access" if user_role =="admin" else "limited access"
print(max_num)
print(min_num)
print(status)
print(temperature)
print(access_level)