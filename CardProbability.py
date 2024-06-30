from random import randint


def method1(card):
    if card % 2 == 0:
        return randint(1, 26) * 2
    else:
        return randint(1, 26) * 2 - 1


def method2(card):
    if card == 1:
        return 1
    else:
        return randint(2, 52)


def generate(n):
    one = 0
    two = 0

    for _ in range(n):
        card = randint(1, 52)
        if method1(card) == card:
            one += 1
        if method2(card) == card:
            two += 1

    print(f"Method 1: {one / n * 100}%")
    print(f"Method 2: {two / n * 100}%")

generate(10000000)