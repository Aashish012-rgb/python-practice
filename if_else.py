# do some code if the condition is true 
# else do something else

#number 01
age= int(input("Enter you r age:"))
if age >=18:
    print("you are now signed up!")
elif age<0:
    print("you are not born yet!")
elif age>=100:
    print("you are too old to sign up!") 
else:
    print("you must be 18 to sign up!")

#number 02
response = input("Do you want to continue? (yes/no): ").strip().lower()
if response == 'yes':
    print("have some food ! ")
elif response == 'no':
    print("okay as you wish!")
else:
    print("please enter valid input ")
#example 3
name = input("Enter your name:")

if name =="":
    print("you didnot enter your name !")
else:
    print(f"Hey {name}")

#exmaple 4
for_sale =True
if for_sale:
    print("tihs item is for sale!")
else:
    print("this item is not for sale!")
    