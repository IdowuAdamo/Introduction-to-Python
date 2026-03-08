ages = (10, 14, 18, 20)  # Immutable: A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets(parentheses).

#ages[0] = 11 
#print(ages)

# looping through all values in a tuple
for age in ages:
    print(age) 
    
# Tuple reassignment 
ages = (10, 14, 18, 20)
print(f"Original tuple {ages}.")

ages = (11, 15, 19, 21)  
print(f"Reassigned tuple {ages}.") 

