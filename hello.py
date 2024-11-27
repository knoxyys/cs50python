def main():
    name = input("What's your name? ") # asks the user for input of their name
    hello(name)

def hello(x):
    x = x.strip().title()
    print(f"hello", x)
    
main()