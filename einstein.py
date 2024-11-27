def main():
    c = 300000000 ## speed of light in m/s
    massInput = int(input("m: "))
    energy = massInput * c**2
    print(f"{energy}")
    
main()