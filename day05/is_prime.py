import sys

num = int(sys.argv[1])

for i in range(2, num + 1):
    if i == num:
        print("True")
        break
    if num % i == 0:
        print("False")
        break
    
