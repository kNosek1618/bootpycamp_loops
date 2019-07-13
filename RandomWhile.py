
from random import randint

number = 0
i = 0
rand = None


while rand != 5:
    rand = randint(1, 10)
    number += 1
    i += 1
    print(f"{number}. {rand}")