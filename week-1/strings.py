"2345" # string
'Ada123678' # string
2345 # not a string
print("Hello World") # string
print(type("Hello World"))# string

# Changing case of strings with methods
name = "caleb"
print(name.title()) # The title() method converts the first character of each word to uppercase and the rest to lowercase.
name = name.title()
print(name)

name = "caleb"
name = name.upper() # The upper() method converts all characters in a string to uppercase.
print(name)

name_1 = "EMMANUELLA" 
name_1 = name_1.lower() # The lower() method converts all characters in a string to lowercase.
print(name_1)

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name # Concatenation of strings
print(full_name)
print(full_name.title()) # Using title() method to capitalize the full name

# Adding whitespace to strings with tabs and newlines
print("My best fruit is Mango")

print("My favorite fruits are: \nMango, \nPineapple, \nWatermelon") # The \n character is used to add a new line in a string.

print('my name is \tEmmaunuella') # The \t character is used to add a tab space in a string.

# Stripping whitespace from strings
user_name = " Caleb"
user_name = user_name.lstrip().lower() # The lstrip() method removes any whitespace characters from the left end of a string.
user_name1 = "CalEb "
print(user_name == user_name1) 
user_name1 = user_name1.rstrip().lower()
print(user_name == user_name1) # The rstrip() method removes any whitespace characters from the right end of a string.

# Avoiding syntax errors with strings
print("I'm learning Python")

