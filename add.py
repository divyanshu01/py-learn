
try:
    a = int(raw_input("first number: "))
    print a
except ValueError:
    print " not an integer"
    exit()

try:
    b = int(raw_input("second number: "))
    print b
except ValueError:
    print " not an integer"
    exit()

print a+b