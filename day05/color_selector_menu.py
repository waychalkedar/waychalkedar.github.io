import sys

colors = ["Blue", "Green", "Yellow", "White"]

try:
    col = sys.argv[1]
except IndexError:
    print("""
      The following colors are available for selection:
      1\tBlue
      2\tGreen
      3\tYellow
      4\tWhite 
      """)
    
    col = input("Enter the number corresponding to your desired color: ")

while(True):
    if col.lower() in ['blue', 'green', 'yellow', 'white']:
        print(f"Chosen color was {col.lower()}")
        break
    
    try:
        num = int(col)
    except ValueError:
        col = input("Please enter an integer number: ")
        continue

    if float(col) != int(col):
        col = input("Please enter an integer, not a floating point number: ")
        continue
    
    if num < 1 or num > 4:
        col = input("Please enter an integer number between 1 to 4: ")
        continue

    print(f"Chosen color was {colors[num - 1]}")
    break




