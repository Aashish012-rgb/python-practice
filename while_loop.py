# while loop = execute some code WHILE some condition remains true

name = input("Enter your name:")
while name == "":
    print(" you didnot entered your name")
    name = input("Enter your name:") # if we didn't retype the prompt we would go on an infinity loop so we use this 

print(f"Hello {name}")

# example 2 ()
age = int(input("Enter your age:"))

while age<0 :
    print("please enter your valid age")
    age = int(input("Enter your age:"))

print(f"you are {age} years old")

# example 3 
food =input("Enter a food you like (q to quit):")
while not food== "q":
    print(f" you like {food}")
    food = input("Enter another food you like (q to quit):")
print("bye")

#example 4
num = int(input("Enter number between 1 to 10:"))

while num <1 or num>10:
    print(f"{num} is nott valid")
    num = int(input("Enter number between 1 to 10:"))
print(f"your number is {num}")
