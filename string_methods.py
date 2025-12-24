#string metods 
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
digit = name.isdigit()
print(digit)
# Treat full name as alphabetic if every word is alphabetic (ignores spaces)
alpha = all(part.isalpha() for part in name.split())
print(alpha)