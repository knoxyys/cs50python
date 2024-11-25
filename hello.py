name = input("What's your name? ") # asks the user for input of their name
name = name.strip() # gets rid of whitespace before and after input
name = name.title() # capitalises first letter of string name (would combine above three lines but for sake of commenting)
print(f"Hello, {name}") # prints the string hello and the variable name (using f string)

# another way to make the print output one line (not using an f string)
print("Hello, ", end="") # 'end' causes a new line to never be created
print(name)

# example of combining lines 2-4
last = input("What's your last name? ").strip().title()
print(f"Hello, {name} {last}") # prints full name after

def hello(x):
    print(f"hello", {x})
    
hello(name) # calls hello function using name variable