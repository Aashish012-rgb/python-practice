# #functions = A block of resuable ode 
# place () after the function name to invoke it

def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"you are {age} years old!")
    print(f"Happy birthday to {name}!")
    print()

happy_birthday("Aashish",20)
happy_birthday("Abhishek",23)
happy_birthday("Zenith",34)


# exmaple 2
def display_invoice(username,amount,due_date):
    print(f"Hello {username}")
    print(f"ypu bill of ${amount:.2f} is due :{due_date}")

display_invoice("Aashish",200,"2025-12-05")
