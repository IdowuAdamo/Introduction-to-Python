print(1+10) # The + operator is used to add two numbers together.
print(17-13) # The - operator is used to subtract one number from another.  
print(30*1) # The * operator is used to multiply two numbers together.
print(15/3) # The / operator is used to divide one number by another. The result is always a float, even if the division is exact. 

print(type(5.0))

print(2**3) # The ** operator is used to raise a number to a power. In this case, 2 raised to the power of 3 is equal to 8.

# The modulus operator
print(13%2) # The % operator is used to find the remainder of a division operation. In this case, 13 divided by 2 leaves a remainder of 1.
print(15%30) # The % operator can also be used when the first number is smaller than the second number. In this case, 15 divided by 30 leaves a remainder of 15, since 30 cannot go into 15 at all.

# Order of operations
print(2+17*2) # In this case, the multiplication is performed before the addition, so the result is 2 + (17 * 2) = 2 + 34 = 36.

# FLOATS
print(30.01 + 0.90)
print(type(30.91))

print(0.1 + 0.2) # This is a common example of a floating-point precision issue in Python. The result is not exactly 0.3 due to the way floating-point numbers are represented in binary.

# Underscores in numbers
a_million = 1_000_000 
print(type(a_million))

# Multiple assignment
a,b,c = 38, 19, 1 
print(a)
print(a/b)
print(b*c)

# Constants
PI = 3.14159 # In Python, constants are typically defined using uppercase letters to indicate that they should not be changed.
print(PI)
print(type(PI))

# The Zen of Python
import this