# number gueesing system 
number = 32

guess_number =int(input("Enter the number:"))

while guess_number !=number:
    guess_number =int(input("Enter the number:"))
    if guess_number == number:
        print("you are great")
    else:
        print("try your best")