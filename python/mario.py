# TODO

def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0 and n <= 8:
                return n
        except ValueError:
            print("Not an integer")

n = get_height() # Need this to assign variable n to an integer from before

for i in range(0, n, 1):
    for j in range (0, n, 1):
        if (i + j < n - 1):
            print(' ', end='') # End parameter prints a newline character after each character so nothing is printed at end of string
        else:
            print('#', end='')

    print() # Make sure this is outside the 2nd for loop to print a newline character after each row
