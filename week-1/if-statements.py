cars = ['Innoson', 'nord', 'Toyota', 'bmw', 'mercedes'] 

for car in cars:
    if car == 'bmw':
        print(car.upper()) 
    else:
        print(car.title()) 
        
# Checking for Equality 
car = 'benz' 
print(car == 'benz')

car = 'benz' 
print(car == 'Benz') # python is case sensitive, so this will return False

car = 'Benz'
print(car.lower() == 'benz') # this will return True because we are converting the string to lower case before comparing it.


# Checking for Inequality 
#age = 19
#print(age != 18)

ordered_item = 'jollof rice'
if ordered_item != 'spaghetti':
    print(f"We don't have {ordered_item}.") 
    
# Numerical Comparisons
print(19 == 19)

print(19 >= 15)

length = 70
print(length <= 70) 

# Checking Multiple Conditions 
# Using "and" to check if two conditions are True
length = 90
length_1 = 150 

print((length >= 90) and (length_1 >= 130)) # True and True will return True

print((length >=91) and (length_1 >= 130)) # False and True will return False

print((length <= 80) and (length_1 <= 130)) # False and False will return false 

# The "or" operator will return True if at least one of the conditions is True 
True or True # will return True
True or False # will return True
False or False # will return False

age = 17
age_1 = 27

print((age <= 18) or (age_1 >= 20)) # True or True will return True
print(age <= 18 or age_1 <= 20) # True or False will return True
print(age >= 18 or age_1 >= 65) # false or False will return False

        
# Checking Whether a Value is in a List
names = ['Donald', 'Emmanuella', 'Ada', 'Caleb'] 
print('idowu' in names)

# Checking Whnether a Value is NOT in a List 
blocked_users = ['ben', 'shade', 'Femi', 'Ada'] 
user = 'ben'
if user not in blocked_users:
    print(f"{user.title()}, you can post a response if you wish.") 
    
# if-else Statements 
blocked_users = ['ben', 'shade', 'Femi', 'Ada'] 
user = 'Caleb'
if user not in blocked_users:
    print(f"{user.title()}, you can post a response if you wish.") 
else:
    print(f"{user.title()}, you are blocked from posting a response.") 
    
age = 90
if age < 18:
    print("You are not yet eligible to vote.") 
    print("Please register to vote as soon as you turn 18.")
else:
    print("You are eligible to vote.") 
    print("Please register to vote as soon as you turn 18.")


# Using "elif" to check multiple conditions
age = 15
if age < 4:
    print("Your ticket is free.")
elif age < 18:
    print("Your ticket costs $5.")
else:
    print("Your ticket costs $15.")
    
# Using Multiple "elif" blocks
age = 40
if age < 4:
    print("Your ticket is free.")
elif age <18:
    print("Your ticket costs $5.")
elif age <65:
    print("Your ticket costs $15.")
else:
    print("Your ticket costs $7.")
    
# Using "elif" blocks with no "else" block
age = 40
if age < 4:
    print("Your ticket is free.")
elif age < 18:
    print("Your ticket costs $5.")
elif age < 65:
    print("Your ticket costs $15.")
elif age >= 65: 
    print("Your ticket costs $7.")
    
# Testing Multiple Conditions  
toppings = ['mushrooms', 'extra cheese', 'onions', 'pepperoni']

if 'mushrooms' in toppings:
    print("Adding mushrooms.")
if 'extra cheese' in toppings:
    print("Adding extra cheese.")
if 'olives' in toppings:
    print("Adding olives.")
if 'pepperoni' in toppings:
    print("Adding pepperoni.")
if 'onions' in toppings:
    print("Adding onions.")
    
print("\nFinished making your pizza!") 

# Working with if statements in a list
requested_toppings = ['mushrooms', 'extra cheese', 'onions', 'pepperoni']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
    
print("\nFinished making your pizza!") 

# Checking if a list is not empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")   
else:
    print("Are you sure you want a plain pizza?") 
        
# Using Multiple Lists 
available_toppings = ['mushrooms', 'extra cheese', 'onions', 'olives', 'pepperoni'] 

requested_toppings = ['mushrooms', 'extra cheese', 'egg'] 

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.") 
        print('Finished making your pizza.') 
    else:
        print(f"We don't have {requested_topping} currently.") 
  
# Styling your code      
if age < 18:
    print('You are eligible to vote.') 
    
    