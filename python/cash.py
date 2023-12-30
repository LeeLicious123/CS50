# TODO

def get_change():
    while True:
        try:
            cents = float(input("Change: ")) # float value as decimals will be involved
            if cents > 0:
                return cents
        except ValueError:
            print("Not an integer")

cents = get_change()

cents = round(cents * 100)

count = 0

while cents >= 25:
    cents = cents - 25
    count += 1

while cents >= 10:
    cents = cents - 10
    count += 1

while cents >= 5:
    cents = cents - 5
    count += 1

while cents >= 1:
    cents = cents - 1
    count += 1

print("Total coins: ", count)
