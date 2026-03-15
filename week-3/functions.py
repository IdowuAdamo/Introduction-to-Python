# A simple function
def greet_users():
    '''Displays a greeting to users.''' # docstring 
    print("Hello!")
    
greet_users() 

# How to Pass Information to a Function
def greet_user(first_name):
    """Displays a personalized greeting to Users."""
    print(f"Hello, {first_name}!")
    
greet_user("Caleb") 
# first_name is the "argument"
# Caleb, Emmanuella or any name provided is the "parameter"

# Passing Arguments   
def pet_details(pet_name, animal_type):
    """Display information about your pet"""
    print(f"My pet is a {animal_type}.") 
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
#pet_details("Dog", "Jack") # Order matters in positional arguments
# pet_details("Jack", "Dog") 

# Passing Arguments   
def pet_details(pet_name, animal_type):
    """Display information about your pet"""
    print(f"My pet is a {animal_type}.") 
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
pet_details(pet_name = "Jack", animal_type = "Dog") 
pet_details(pet_name = 'Dill', animal_type = "Rabbit")

# Default values
def favorite_sport(first_name, sport="football"): 
    """Displays the favorite game of the user"""
    print(f"My favorite sport is {sport}.")
    print(f"{first_name}'s favorite sport is {sport}") 
    
favorite_sport(first_name = "ELizabeth", sport = "Lawn Tennis")

# Avoiding Argument Errors
def favorite_sport(first_name, sport="football"): 
    """Displays the favorite game of the user"""
    print(f"My favorite sport is {sport}.")
    print(f"{first_name}'s favorite sport is {sport}") 
    
# favorite_sport() # This results in an error, because the first_name nedds to be specified
#favorite_sport("John", "Volleyball", "basket ball") # results in an error because the function takes from 1 to 2 positional arguments but 3 were given

# Returning a simple Value
def format_name(first_name, last_name):
    """Returns the full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title() 

full_name = format_name('ada', 'lovelace') 
print(full_name) 

# Making an Argument Optional
def format_name(first_name, last_name, middle_name=""):
    """Returns the full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name 

full_name = format_name('Johnson', 'King') 
print(full_name) 

# Return a dictionary
def format_user(first_name, last_name, middle_name=""):
    """Returns a dictionary of information about the user"""
    if middle_name:
        full_name = {"first":first_name,  "middle":middle_name, "last":last_name}
    else:
        full_name = {"first":first_name, "last":last_name}
    return full_name 

user_1 = format_user("ada", "lovelace")
print(user_1)

# Using a function with a while loop
def get_full_name(first_name, last_name):
    """Returns a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}" 
    return full_name.title() 

#while True:
    #print("\nTell me your name: ") 
    #_name = input("First name: ")
    #if f_name == "quit":
        #break
    
    #l_name = input("Last name: ")
    #if l_name == "quit":
        #break
    
    #formatted_name = get_full_name(f_name, l_name)
    #print(f"Hello, {formatted_name}.")
    
# Passing a List
def greet_user(names):
    '''Displays a simple greeting to each user in the list'''
    for name in names:
        message = f"Hello {name.title()}"
        print (message) 
        
users = ['Ben', 'Olu', 'Johnson']
greetings = greet_user(users) 
print(greetings) 

# Modifying a list in a Function 
#unverified_users = ['john_18', 'thompson1', 'ben', 'shehu']
#verified_users = ['caleb', 'emmanuella', 'ada'] 

#while unverified_users:
    #user = unverified_users.pop() 
    #print(f"Verifying {user}.") 
    #erified_users.append(user) 
    
# Display the verified users
#print("\n The following users are verified: ")
#for verified_user in verified_users:
    #print(verified_user) 
    

def verify_users(unverified_users, verified_users):
    """Verifies unverified users by adding them to the list of verified users"""
    while unverified_users:
        current_user = unverified_users.pop() 
        print(f"Verifying {current_user}.") 
        verified_users.append(current_user) 
        
def show_verified_users(verified_users):
    """Shows verified users."""
    print("\n The following users are verified: ")
    for verified_user in verified_users:
        print(verified_user) 
    
# Modifying a list in a Function 
unverified_users = ['john_18', 'thompson1', 'ben', 'shehu']
verified_users = ['caleb', 'emmanuella', 'ada'] 

verify_users(unverified_users[:], verified_users) # Preventing a Function from modifying a List
show_verified_users(verified_users) 

print(unverified_users)
print(verified_users)



# Making a function with an arbitrary number of arguments
def make_pizza(*toppings):
    """List the requested toppings"""
    print(toppings) 
    
make_pizza('Cheese')
make_pizza('Onions', 'green peppers', 'cheese') 

# Mixing positional and arbitrary arguments
def make_pizza(size, *toppings):
    '''Summarize the order'''
    print(f"Making a {size.title()} pizza with the following toppings: ")
    for topping in toppings:
        print(f" {topping}") 
        
make_pizza("jumbo", 'Onions', 'green peppers', 'cheese')

def favorite_sport(first_name, *sports): 
    """Displays the favorite game of the user"""
    print(f"My favorite sport is {sports}.")
    print(f"{first_name}'s favorite sport is/are: ") 
    
    for sport in sports:
        print(f" {sport}")
    
favorite_sport("ELizabeth", "Lawn Tennis", "Badmiton")

