import sys
try:
    a = int(input("first number: "))
except ValueError:
    print("not an integer")
    sys.exit(1)

try:
    b = int(input("second number: "))
except ValueError:
    print("not an integer")
    sys.exit(1)

print(a+b)
