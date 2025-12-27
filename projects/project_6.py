# ATM menu programs hints 
try: # loads balance ffrom file 
    with open("balance.txt", "r") as file:
        Balance = float(file.read())
except FileNotFoundError:
    Balance = 0.00

while True:
    print("=====ATM Menu=====")
    print("1.check balnce")
    print("2.Deposite")
    print("3.withdraw")
    print("4.Exit")

    choice = input("Enter the choice(1,2,3,4):")

    if choice== "1":
        print(f"you have  ${Balance} balance in youe account")
    elif choice== "2":
        amount = float(input("Ente rthe amount, you want to deposite:"))
        if amount > 0:
            Balance += amount
            print(f"you balance after deposite is ${amount}")
        else:
            print("invalid amount to deposite!")
    elif choice== "3":
        amount=float(input("Enter the amount you want to withdraw:"))
        if amount>0:
            if amount<=Balance:
                Balance -= amount
                print(f" Withdrawn {amount:.2f}. Remaining balance: ${Balance:.2f}")
            else:
                 print("Insufficuent Balance!")
        else:
           print("Invalid withdrawal amount")
    elif choice==4:
        print("Thank you for using ATM! visit again ")
        break
    else:
        print("Invalid choice! please enter a valid number(1,2,3,4):")

        