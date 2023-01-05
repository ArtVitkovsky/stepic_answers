def the_first():
    for hours in range(24):
        for minutes in range(60):
            for seconds in range(60):
                print(f'hours: {hours} minutes: {minutes} seconds: {seconds}')


def the_second():
    flag = True
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            print(i, j)


def the_third():
    for i in range(8):
        for j in range(6):
            print('*', end='')
        print()


def the_fourth():
    for i in range(8):
        for j in range(i + 1):
            print('*', end='')
        print()


def the_fifth():
    for i in range(1, 6):
        for j in range(3, 6):
            print(i, j)


def the_sixth():
    for i in range(1, 4):
        for j in range(3, 5):
            print(i + j, end='')


def the_seventh():
    counter = 0
    for i in range(99, 102):
        temp = i
        while temp > 0:
            counter += 1
            temp //= 10
    print(counter)


def the_eighth():
    import math as m
    n = 5
    center = n // 2 + 1
    count = 0
    for i in range(1, n + 1):
        if i > center:
            count -= 1
        else:
            count += 1
        for j in range(count):
            print('*', end='')
        print()


def the_ninth():
    n = 5
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end='')
        print()


