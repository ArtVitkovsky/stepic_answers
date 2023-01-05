# This is a file with the solution of knowledge of the "python generation" course. Chapter 13. Theme: "Functions".

# Task 1 write a function that cuts a rectangle 14 x 10

def draw_box_1():
    print('*' * 10)
    for i in range(12):
        print('*' + (' ' * 8) + '*')
    print('*' * 10)


# Task 2: write a function that cuts triangle

def draw_triangle():
    a = 1
    while a <= 10:
        print('*' * a)
        a += 1


# Task 3: write function with options. Draw a triangle


def draw_triangle_1(fill, base):
    for i in range(1, base + 1):
        print(fill * min(i, base - i + 1))


# Task 4: write function leading PHIL


def print_fio(name, surname, patronymic):
    print(name.upper()[0] + surname.upper()[0] + patronymic.upper()[0])


# Task 5: write function that convert km to miles


def convert_to_miles(km):
    miles = km * 0.6214
    return miles


# Task 5: write function return number of days in a month


def get_days(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 10:
        return 30
    else:
        return 28


# Task 6: write a function that returns the divider of the given number


def get_factors(num):
    lst = []
    for i in range(1, num + 1):
        if num % i == 0:
            lst.append(i)
    return lst, len(lst)


# Task 7: write a function that finds all positions of the given litter

def find_all(target, symbol):
    return [c for c in range(len(target)) if target[c] == symbol]


# Task 8: write a function that a sorted list


def merge(list1, list2):
    return sorted(list1 + list2)


# Task 9: is a number prime

def is_prime(num):
    return len([i for i in range(1, num + 1) if num % i == 0]) == 2


# Task 10: good password:

def is_password_good(password):
    up = [i for i in password if i.isupper()]
    low = [i for i in password if i.islower()]
    dig = [i for i in password if i.isdigit()]
    return all([len(password) >= 8, up, low, dig])


# Task 11:

def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    c = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            c += 1
    if c <= 1:
        return True
    else:
        return False


# Task 12: search a palindrome

def is_palindrome(text):
    text = [i.lower() for i in text if i not in (',.!?- ')]
    return text == text[::-1]


# Task 13: search a middle point

def get_middle_point(r):
    import math as m
    c = 2 * (m.pi * r)
    s = m.pi * (r ** 2)
    return c, s
