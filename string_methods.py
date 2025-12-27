# #string metods 
name = input("Enter your full name:")

result =len(name)
result = name.find("A") #for first occurence
answer = name.rfind("h")#for last occurence
name = name.capitalize() #to capitalize
print(result)# for first occurence
print(answer) #for last occurence
print (name) #for capitalize
aashish = name.upper()
print(aashish)
digit = name.isdigit()# to check whether there is digit or not 
print(digit)
alpha = name.isalpha()# to check whether there  is alphabet of not  
print(alpha)
# output = false because it contains false 
phone_number =input("Enter your phone number:")

# result= phone_number.count("-") #use to count
result= phone_number.replace("-"," ") #to replace something with something

print(result)
#print(help(str)) #used for viewing 
