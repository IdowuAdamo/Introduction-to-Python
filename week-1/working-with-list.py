names = ['Caleb', 'Emmanuella', 'ada'] 

for name in names:
  print(name) 
  
for name in names: 
  print(f"Hello {name.title()}!") # The f-string is used to format a string by including the value of a variable inside the string. In this case, it will print "Hello Caleb!", "Hello Emmanuella!", and "Hello Ada!" for each name in the list.
  
names = ['Caleb', 'Emmanuella', 'ada']
for name in names:
  print(f"Hello {name.title()}")
  print(f"It is really nice to meet you {name.title()}!\n") # The \n is used to add a new line after each greeting, making the output more readable. It will print "Hello Caleb!", "It is really nice to meet you Caleb!", "Hello Emmanuella!", "It is really nice to meet you Emmanuella!", "Hello Ada!", and "It is really nice to meet you Ada!" with a blank line in between each greeting.
print("Thank you everyone for joining us today!") # This will print a final message after the loop has finished executing, thanking everyone for joining.

# Avoiding identation errors
ages = [10, 17, 13, 11, 13, 19]
# Forgetting to indent the block of code inside the for loop will result in an IndentationError. In this case, the print statement is not indented, so it will cause an error when the code is executed.
#for age in ages:
#print(age) 

# Unnecessary indentation 
#message = "Hello everyone!"
  #print(message) 

# Indenting unecessarily 
names=['Caleb', 'Emmanuella', 'ada'] 
for name in names:
  print(f"Hello {name.title()}")
  print(f"It is really nice to meet you {name.title()}!\n")
 #print("Thank you everyone for joining us today!")
 
# Forgetting the colon
ages = [10, 17, 13, 11, 13, 19]
#for age in ages
  #print(age)
  
# How to work with numbers in list 
for number in range(1,10):
  print(number) # The range() function is used to generate a sequence of numbers. In this case, it will generate numbers from 1 to 9 (the stop value is exclusive). The for loop will iterate through each number in the range and print it.
  
ages = list(range(10,20)) # The range() function can also be used to create a list of numbers by converting the range object to a list using the list() function. In this case, it will create a list of ages from 10 to 19.
print(ages) 

even_numbers = list(range(2,16,2)) # The range() function can also take a step parameter to specify the increment between numbers in the sequence. In this case, it will generate even numbers from 2 to 14 by starting at 2 and incrementing by 2.
print(even_numbers)

for number in range(1,15):
  print(number**2) # The ** operator is used to raise a number to a power. In this case, it will print the square of each number from 1 to 14. 
  
# List comprehesions(allow to create a new list by applying an expression to each item in an iterable)
squares = [number ** 3 for number in range(1,15)] # This is a list comprehension, which is a concise way to create a new list by applying an expression to each item in an iterable. In this case, it will create a list of squares for numbers from 1 to 14.
print(squares)

# Simple statistics with a list of numbers 
ages = [10, 17, 13, 11, 13, 19]
print(min(ages)) # The min() function is used to find the smallest number in a list. In this case, it will return 10, which is the youngest age in the list. 

popped_age = ages.pop(0) 
print(min(ages)) # After removing the youngest age (10) from the list using the pop() method, the min() function will now return 11, which is the next youngest age in the list.

# maximum number in a list
ages = [10, 17, 13, 11, 13, 19] 
print(max(ages)) # The max() function is used to find the largest number in a list. In this case, it will return 19, which is the oldest age in the list. 

ages.append(70)
print(max(ages)) # After adding a new age (70) to the list using the append() method, the max() function will now return 70, which is the new oldest age in the list.

# sum of numbers in a list 
ages = [10, 17, 13, 11, 13, 19] 
print(sum(ages)) # The sum() function is used to calculate the total of all the numbers in a list. In this case, it will return 83, which is the sum of all the ages in the list. 

print(10+ 17+ 13+ 11+ 13+ 19)


# Working with part of a list
names = ['Caleb', 'Ada', 'Emmanuella', 'John', 'Phillip']

# Slicing
print(names[0:3]) # The slicing syntax [start:stop] is used to access a portion of a list. In this case, it will return a new list containing the first three names: ['Caleb', 'Ada', 'Emmanuella']. The start index is inclusive, while the stop index is exclusive.

print(names[1:4]) # This will return a new list containing the names from index 1 to index 3: ['Ada', 'Emmanuella', 'John'].

# Omitting the start index
print(names[:4]) # If the start index is omitted, it defaults to 0. In this case, it will return a new list containing the first four names: ['Caleb', 'Ada', 'Emmanuella', 'John']. 

# Omitting the stop index 
print(names[1:])

# Looping through a slice 
print("The AI Engineers in my team are:") 
for name in names[:3]:
  print(f"{name.title()}") 
  
# Copying a list
my_favorite_games = ['Chess', 'Scrabble', 'Monopoly']  
my_friends_favorite_games = my_favorite_games[:] 

print(my_favorite_games) 
print(my_friends_favorite_games) 

my_friends_favorite_games.append('Whot') 
print(my_favorite_games) 
print(my_friends_favorite_games) 

my_favorite_sports = ['Football', 'Basketball', 'Tennis']
my_friends_favorite_sports = my_favorite_sports # Another way  to copy a list is to simply assign it to a new variable. However, this creates a reference to the original list rather than a new copy. Therefore, any changes made to my_friends_favorite_sports will also affect my_favorite_sports since they both refer to the same list in memory. 

print(my_favorite_sports)
print(my_friends_favorite_sports) 

my_friends_favorite_sports.append('Volleyball')

print(my_favorite_sports)
print(my_friends_favorite_sports) 


