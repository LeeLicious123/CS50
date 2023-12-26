# TODO

def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0 and n <= 8:
                return n
        except ValueError:
            print("Not an integer")

n = get_height()

for i in range(0, n, 1):
    for j in range (0, n + 3 + i, 1):
        if (n == j or j == n+1 or i+j < n-1):
            print(' ', end='') # End parameter prints a newline character after each character so nothing is printed at end of string
        else:
            print('#', end='')
    print()
