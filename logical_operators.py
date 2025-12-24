# logical operartors = evaluate multiple conditions(or, and, not )
#                 or = at least one condition must be True 
#                 and = both conditions must be true 
#                 not = inverts the conditions (not False, not True)
#or logical operator
temp = 42
is_raining = False

if temp>35 or temp<0 or is_raining:
    print("The event id cancelled")
else:
    print("The event is still scheduled")

#and logical operator  
temp = 28
is_sunny = False

if temp>= 28 and is_sunny:
    print("It is hot outside")
    print("it is sunny")
elif temp<=0 and is_sunny:
    print("it is cold outsdie")
    print("it is sunny")
elif temp<28 and temp>0 and is_sunny:
    print("it is warm outside")
    print("it is sunny")

#not logical operator
elif temp>= 28 and not is_sunny:
    print("It is hot outside")
    print("it is cloudy")
elif temp<=0 and not is_sunny:
    print("it is cold outside")
    print("it is cloudy")
elif temp<28 and temp>0 and not is_sunny:
    print("it is warm outside")
    print("it is cloudy")
else:
    print("It is not the valid")
  