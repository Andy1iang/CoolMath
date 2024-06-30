from random import randint


def switch(door):
    choice = randint(0, 2)
    if choice == door:
        return False
    else:
        return True


def noSwitch(door):
    choice = randint(0, 2)
    if choice == door:
        return True
    else:
        return False


def generate(n):
    one = 0
    two = 0

    for _ in range(n):
        door = randint(0, 2)
        if switch(door):
            one += 1
        if noSwitch(door):
            two += 1

    print(f"Switch: {one / n * 100}%")
    print(f"No Switch: {two / n * 100}%")


generate(10000000)
