
x = 0

for n in range(20):
    x = x + 1
    if x != 4 and x != 13:
        if x % 2 != 0:
            print(f"{x} is odd")
        else:
            print(f"{x} is even")
    else:
        print(f"{x} is UNLUCKY!")
