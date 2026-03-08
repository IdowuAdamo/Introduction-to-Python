#age = 18
#if age >= 18:
    #print('You are eligible to Vote!') 
    #print('Have you registered to vote.')
#else:
    #print('You are not yet eligible to vote')
    #print('Register to vote as soon as you turn 18.')
    
# User Inputs
#print(input('Tell me something, and I will repeat it back to you:'))

# Writing clear prompts
#prompt = "Tell me your name and I will personalize a message for you"
#prompt += "\n What is your name:"
#name = input(prompt) 

#print(f"Hello {name}!") 


# Using 'int()' method to accept numerical inputs
#age = input('How many years old are you:')
#age = int(age) 
#print(age)
#print(type(age))  

#print(age >= 18)

#age = input("How many years old are you:")
#age = int(age) 

#if age >= 18:
    #print('You are eligible to Vote!') 
    #print('Have you registered to vote.')
#else:
    #print('You are not yet eligible to vote')
    #print('Register to vote as soon as you turn 18.')
    
# The Modulo Operator
print(13%5)
print(3%4)

# Odd or Even
#number = input("Input a number, and I will tell you if it is Even or Odd: ") 
#number = int(number) 

#if number%2 == 0:
    #print(f"{number} is Even.")
#else:
    #print(f"{number} is Odd; not divisible by 2") 
    
    
# While Loops
#number = 1
#while number <5:
    #print(number)
    #number += 1
    
# Allowing the User to choose when to Quit
#prompt = "Tell me something, and I will repeat it back to you: "
#prompt += "\nEnter 'quit' to stop the Program! " 

#message = ''
#while message != 'quit':
    #message = input(prompt)
    #print(message) 
    
# Using a Flag
#prompt = "Tell me something, and I will repeat it back to you: "
#prompt += "\nEnter 'quit' to stop the Program! " 

#message = ''
#active = True
#while active:
    #message = input(prompt)
    #if message == 'quit':
        #active = False
    #else:  
        #print(message)
        
# Using 'break' to Exit a While Loop
prompt = "Input the name of a city you have visited and I will personlaize a message for you"
prompt += "\nEnter 'quit' when you have finished."

while True:
    city = input(prompt)
    
    if city == 'quit':
        break 
    else:
        print(f"I have visited {city}!") 
        
print(2+2)