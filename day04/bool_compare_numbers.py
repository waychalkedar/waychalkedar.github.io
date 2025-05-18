n1 = input("Enter a number: ")
n2 = input("Enter a second number: ")

try: 
    if int(n1) < int(n2):
        print(f"{n1} is smaller than {n2}")
    elif int(n1) > int(n2):
        print(f"{n1} is greater than {n2}")
    else:
        print(f"{n1} is equal to {n2}")
    
except ValueError:
    print("Please enter a number") 