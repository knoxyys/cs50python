x = float(input("x = "))
y = float(input("y = ")) # blah blah gets input

add = round(x + y)
divide = round(x / y, 2) # the 2 specifies the amount of decimal points to round to

print(f"x + y = {add:,}") # colon is a separator for formatting, comma a builtin thousands separator i think?
print(f"x / y = {divide:.2f}") # .2 specifies the decimal places (forces it, will fill with 0 if not needed), f specifies float