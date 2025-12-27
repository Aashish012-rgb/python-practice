# indexing = accessing elements of a sequence using [] (indexing operator)
# [Start: end: step]

credit_number = "1234-4567-7890-1245"

# print(credit_number[0]) #to get the inde number 


print(credit_number[0:4]) #to print the number 1234
print(credit_number[5:9]) # to print the number 4567
print(credit_number[5:]) #to print from a index to last 
print(credit_number[-1]) # it does form the back of that number  // we canuse negative indexes too 
print(credit_number[::2]) # this print everyu second characters of our string 
last_digit = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digit}") # to print from the last digits 
credit_number =credit_number[::-1] # to reverse te string 
print(credit_number)
