names = ['Emmanuella','Caleb','Idowu']
print(names)
print(type(names)) # The type() function is used to determine the type of a variable. In this case, it will return <class 'list'>, indicating that names is a list.
names_0 = names[0]
print(names_0)
# Number of elements in a list
print(len(names)) # The len() function is used to determine the number of elements in a list. In this case, it will return 3, since there are three names in the list.

print(f"Hello {names_0}") # The f-string is used to format a string by including the value of a variable inside the string. In this case, it will print "Hello Emmanuella", since names_0 contains the value 'Emmanuella'.


# Modifying, Adding and Removing Elements in a List
names = ['Emmanuella','Caleb','Idowu']
names[2] = 'Ada'
print(names) # This will change the value of the third element in the list from 'Idowu' to 'Ada'.

# Adding elements to a list
car_brands = ['Innoson','Toyota','Nord','Mercedes','Tesla']
print(car_brands)
car_brands.append('Lexus')
print(car_brands)

car_brands.insert(1, 'Honda') # The insert() method is used to add an element at a specific position in the list. In this case, it will insert 'Honda' at index 1, which is the second position in the list.
print(car_brands)

# Removing elements from a list
car_brands.remove('Mercedes') # The remove() method is used to remove the first occurrence of a specified value from the list. In this case, it will remove 'Mercedes' from the list.
print(car_brands)

car_brands.pop(1) # The pop() method is used to temporarily remove an element at a specific index from the list. In this case, it will remove the element at index 1, which is 'Honda'.
print(car_brands)
popped_brand = car_brands.pop() # If no index is specified, the pop() method will remove the last element from the list. In this case, it will remove 'Lexus' from the list and store it in the variable popped_brand.
print(car_brands)
print(popped_brand)

del car_brands[-1] # The del statement is used to delete an element at a specific index from the list. In this case, it will delete the last element from the list, which is 'Tesla'.
print(car_brands)


# Organizing a List
ages = [10, 17, 13, 11, 13, 19]
ages.sort() # The sort() method is used to permanently sort the elements of a list in ascending order. In this case, it will sort the ages from youngest to oldest.
print(ages) 

ages = [10, 17, 13, 11, 13, 19]
ages.sort(reverse=True) # The sort() method can also be used to sort the elements of a list in descending order by setting the reverse parameter to True. In this case, it will sort the ages from oldest to youngest.
print(ages)

names = ['Emmanuella','Caleb','Ada']
names.sort() # The sort() method can also be used to sort a list of strings in alphabetical order. In this case, it will sort the names in alphabetical order.
print(names) 

ages_ordered1 = ages.sort()
print(ages_ordered1) # The sort() method does not return a new list, it modifies the original list in place and returns None. Therefore, ages_ordered1 will be None, and the original ages list will be sorted.

# Temporarily sorting a list with the sorted() function
ages = [10, 17, 13, 11, 13, 19]
ages_ordered = sorted(ages) # The sorted() function is used to temporarily sort the elements of a list in ascending order without modifying the original list. In this case, it will return a new list with the ages sorted from youngest to oldest, while the original ages list remains unchanged.

print(ages)
print(ages_ordered) 

age = [10, 17, 13, 11, 13, 19] 
ages_sorted_reverse = sorted(ages, reverse=True) # The sorted() function can also be used to sort the elements of a list in descending order by setting the reverse parameter to True. In this case, it will return a new list with the ages sorted from oldest to youngest, while the original ages list remains unchanged.
print(ages_sorted_reverse) 

names = ['Emmanuella','Caleb','Ada']
names.append('Idowu') 
names_sorted = sorted(names) # The sorted() function can also be used to sort a list of strings in alphabetical order. In this case, it will return a new list with the names sorted in alphabetical order, while the original names list remains unchanged.
print(names_sorted) 

names_sorted_reverse = sorted(names, reverse=True) # The sorted() function can also be used to sort a list of strings in reverse alphabetical order by setting the reverse parameter to True. In this case, it will return a new list with the names sorted in reverse alphabetical order, while the original names list remains unchanged.
print(names_sorted_reverse) 

# Reversing the order of a list
ages = [10, 17, 13, 11, 13, 19] 
ages.reverse() # The reverse() method is used to permanently reverse the order of the elements in a list. In this case, it will reverse the order of the ages in the list.
print(ages)

names = ['Emmanuella','Caleb','Ada']
names.insert(0, 'Johnson') 
names.reverse() # The reverse() method can also be used to reverse the order of a list of strings. In this case, it will reverse the order of the names in the list.
print(names) 

# Finding the length of a list 
ages = [10, 17, 13, 11, 13, 19]  
ages.remove(13) # The remove() method is used to remove the first occurrence of a specified value from the list. In this case, it will remove the first occurrence of 13 from the list.
 
print(len(ages)) # The len() function is used to determine the number of elements in a list. In this case, it will return 6, since there are six ages in the list. 

# How to avoid Index Error when working with lists
ages = [10, 17, 13, 11, 13, 19]
#print(ages[6]) 

print(ages[-1]) 


