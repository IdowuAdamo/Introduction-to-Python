# Using 'continue' in a loop
#current_number  = 0
#while current_number < 20:
    #current_number += 1
    #if current_number % 2 == 0:
        #continue
    
    #print(current_number) 
    
    
# Avoiding Infinite Loops
#current_number = 0
#while current_number < 5:
    #print(current_number)
    #current_number += 1 
    
# Infinite Loop
#current_number = 0
#while current_number < 5:
    #print(current_number)
      
# Using a while loop with Lists and Dictionaries
# Moving items from one list to another

unverified_users = ['ada_lovelace', 'john_scout1', 'odogwu107'] 
verified_users = ['Caleb', 'Emmauella'] 

while unverified_users:
    current_user = unverified_users.pop() 
    
    print(f"Verifying {current_user}!")
    verified_users.append(current_user)
    
# Display the verified users
print ("\nThe following users are verified: ")
for verified_user in verified_users:
    print(verified_user)
    
# Removing all instances of specific values from a list

# removes only first occurence
favorite_games = ['chess', 'monopoly', 'scrabble', 'chess', 'scrabble', 'whot']
favorite_games.remove('chess') 
print(favorite_games) 

# removes all occurence of specific value
while 'scrabble' in favorite_games:
    favorite_games.remove('scrabble')
    
print(favorite_games) 

# Filling a Dictionary with User Inputs
responses = {}
collecting_responses = True 

while collecting_responses:
    name = input("What is your name?")
    city = input("Where do you live?") 
    
    # store the response in our dictionary
    responses[name] = city 
    
    repeat = input("Would you like anyone else to take this poll? (yes/no)")
    if repeat == 'no':
        collecting_responses = False 
        
    # Show responses
    print("Poll results")
    
    for name, city in responses.items():
        print(f"{name.title()} lives in {city.title()}.")