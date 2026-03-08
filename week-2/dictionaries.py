person_1 = {'age':15, 'first_name':'Ada', 'last_name':'Lovelace'} # key-value pairs in a dictionary 

# Accessing values in a dictionary
print(person_1['first_name'])  

print(person_1['age'])

simple_dict = {'name': 'John'} 

# Adding new key-value pairs to a dictionary
simple_dict['age'] = 80
print(simple_dict)

# Starting with an empty dictioary and adding key-value pairs
person_2 = {}
person_2['first_name'] = 'Phillip' 
person_2['last_name'] = 'Emeagwali'
person_2['age'] = 70
print(person_2)

# Modifying values in a dictionary
person_2['age'] = 71 
print(person_2)

# Removing key-value pairs from a dictionary 
alien_1 = {'color': 'red', 'points': 10, 'speed': 'fast'} 
print(alien_1)
del alien_1['points'] 
print(alien_1) 

# A dictionary of Similar items
favorite_games = {
    'Ada': 'Chess',
    'John': 'Football',
    'David': 'Ludo',
    'Victoria': 'Scrabble'
    
}

# Accessing values using the get method
user_1 = {'username':'Id_noble', 'age': 19, 'first_name':'Idowu', 'last_name':'Adamo'}
print(user_1['age']) 

#print(user_1['location']) 
user_location = user_1.get('location')
print(user_location) 

user_location = user_1.get('location', 'location has not been defined in the dictionary')
print(user_location) 

user_location = user_1.get('first_name', 'first name has not been defined')
print(user_location) 

# Looping through a Dictionary 
for key, value in user_1.items():
    print(f"Key: {key}")
    print(f"Value: {value}") 
    
favorite_games = {'Caleb':'Chess', 'Emmanuella':'ludo', 'Johnson':'Scrabble', 'Phillip':'ludo'} 

for name, favorite_game in favorite_games.items():
    print(f"{name} favorite game is {favorite_game}.")
    
# Looping through all the keys in a Dictionary
for name in favorite_games.keys():
    print(f"{name}")
    
for name in favorite_games.keys():
    print(f"{name.title()}, thank you for taking the survey.")
    
friends = ['Emmanuella', 'Caleb'] 
for name in favorite_games.keys():
    print(f"Hello {name}!")
    
    if name in friends:
        favorite_game = favorite_games[name].title() 
        print(f"{name.title()}, I see you love {favorite_game}.")
        
# Looping through a Dictionary in a Particular order
favorite_games = {'Caleb':'Chess', 'Emmanuella':'ludo', 'Johnson':'Scrabble', 'Phillip':'ludo'} 

for name in sorted(favorite_games.keys()):
    print(f"{name.title()}, thank you for taking the survey.")
    
# Looping through all the values in a Dictionary
print("These have been mentioned:")
for favorite_game in favorite_games.values():
    print(f"{favorite_game}")
    
print("These have been mentioned:")
for favorite_game in set(favorite_games.values()):
    print(f"{favorite_game}")
    
favorite_games = {'ludo','chess','tennis','chess','tennis'}
print(favorite_games) 

# Nesting
user_1 = {'username':'Id_noble', 'age': 19, 'first_name':'Idowu', 'last_name':'Adamo'}
user_2 = {'username':'ada_lvl', 'age': 23, 'first_name':'Ada', 'last_name':'Lovelace'}

users = [user_1, user_2]
print(users)

# nesting a list in a dictionary
user_3 = {'username':'Id_noble', 'age': 19, 'first_name':'Idowu', 'last_name':'Adamo', 'favorite_games':['volleyball','scrabble']} 
print(user_3)

# nesting a dictionary in a list
aliens = []

for alien_number in range(30):
    new_alien = {'color':'yellow', 'points': 15, 'speed':'very fast'}
    aliens.append(new_alien) 
    
print(len(aliens))

print(aliens[:5]) 

for alien in aliens[:10]:
    if alien['color'] == 'yellow':
        alien['color'] = 'blue'
        alien['points'] = 30
        alien['speed'] = 'fast'
        
print(aliens[:15])


# A list in a dictionary
user_4 = {'name':'Ben', 'games':['football','basketball','table tennis']}

print(f"{user_4['name']} plays these games:") 

for game in user_4["games"]:
    print(f"\t{game.title()}") 
    
# Nesting Dictionaries in a Dictionary
people = {
    'ada_lovelace' :{'first_name': 'Ada', 
                     'last_name':'lovelace', 'age':'12'},
    
    'john_walker' :{'first_name': 'John',
                   'last_name':'walker', 'age':'10'},
}
print(people)


for key, value in people.items():
    print(key)
    full_name = f"{value['first_name']} {value['last_name']}"
    age = value["age"]
    
    print(f"\tFull Name: {full_name}")
    print(f"\tAge: {age}") 