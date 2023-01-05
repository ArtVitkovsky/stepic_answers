# This is a file with the solution of knowledge of the "python generation" course. Chapter 11.4

# Task 1: print the sum of the squares of the list
def the_first():
    numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
    print(sum([i ** 2 for i in numbers]))


# Task 2: write a program that inserts input numbers instead of x
def the_second():
    n = 5
    lst = []
    for i in range(n):
        x = int(input())
        f = (x ** 2) + (2 * x) + 1
        lst.append(f)
    print(*lst, sep='\n')


# Task 3: deleting minimum and maximum values

def the_third():
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(int(input()))
    for j in lst:
        if j != min(lst) and j != max(lst):
            print(j)


# Tack 4: print only unique strings

def the_fourth():
    n = int(input())
    lst = []
    for i in range(n):
        s = input()
        if s not in lst:
            lst.append(s)
            print(s)


# Task 5

def the_fifth():
    n = int(input())
    lst = []
    search = input().lower()
    for i in range(n):
        s = input()
        lst.append(s)
    for j in lst:
        if search in j:
            print(j)


# Task 6: print the negative, zero and positive

def the_sixth():
    n = int(input())
    neg = []
    zer = []
    pos = []
    for i in range(n):
        num = int(input())
        if num < 0:
            neg.append(num)
        if num == 0:
            zer.append(num)
        if num > 0:
            pos.append(num)
    print(*neg, sep='\n')
    print(*zer, sep='\n')
    print(*pos, sep='\n')


# Task 7: print string like a column

def the_seventh():
    s = 'У лукоморья дуб зеленый златая цепь на дубе том'
    lst = s.split()
    print('\n'.join(lst))


# Task 8: print initials

def the_eighth():
    s = 'Владимир Семенович Высоцкий'
    lst = []
    for c in s:
        if c.istitle():
            lst.append(c)
    print('.'.join(lst))


# Task 9: print string like a column

def the_ninth():
    s = 'C:\Windows\System32\calc.exe'
    lst = s.split(chr(92))
    print('\n'.join(lst))


# Task 10: building of a diagram

def the_tenth():
    s = '1 2 3 4 5'
    for i in s.split():
        print('*' * int(i))


# Task 11: determine the correctness of the IP address

def the_eleventh():
    s = '192.168.0.2'
    flag = True
    for i in s.split('.'):
        if 0 <= int(i) <= 255:
            flag = True
        else:
            flag = False
    if flag is True:
        print('ДА')
    else:
        print('НЕТ')


# Task 12: use the specified delimiter

def the_twelfth():
    s = input()
    sep = input()
    print(sep.join(s))


# Task 13: developing list functions

def the_thirteenth():
    numbers = [8, 9, 10, 11]
    numbers[1] = 17
    numbers.append(4)
    numbers.append(5)
    numbers.append(6)
    numbers.remove(8)
    numbers.extend(numbers)
    numbers.insert(3, 25)
    print(numbers)


def the_fourteenth():
    s = '3 4 5 2 1'
    lst = s.split()
    a = lst.index(max(lst))
    b = lst.index(min(lst))
    lst[a], lst[b] = min(lst), max(lst)
    print(lst)


def the_fifteenth():
    s = 'William Shakespeare was born in the town of Stratford, England, in the year 1564. When he was a young man,' \
        ' Shakespeare moved to the city of London, where he began writing plays. His plays were soon very successful,' \
        ' and were enjoyed both by the common people of London and also by the rich and famous. In addition to his ' \
        'plays, Shakespeare wrote many short poems and a few longer poems. Like his plays, these poems are still' \
        ' famous today.'
    lst_2 = []
    lst = s.split()
    for i in lst:
        if i == 'a' or i == 'an' or i == 'the':
            lst_2.append(i)
    print(f'Общее количество артиклей {len(lst_2)}')


# Task 16: sorting lists

def the_sixteenth():
    s = '4 5 1 2 3 8'.split()
    for i in range(len(s)):
        s[i] = int(s[i])
    s.sort()
    print(*s)
    s.sort(reverse=True)
    print(*s)

# Task 17: get a list with swift characters


def the_seventeenth():
    s = ['Artem', 'Sasha', 'Oleg', 'Roma', 'Sergey']
    st = [len(i) for i in s]
    print(st)


# Task 18: lists with additional conditions


def the_eighteen():
    s = ['Artem', 'Sasha', 'Oleg', 'Roma', 'Sergey']
    st = [i for i in s if len(i) >= 5]
    print(st)


# Task 19: get list with palindromes

def the_nineteenth():
    palindromes = [i for i in range(100, 1000) if str(i) == str(i)[::-1]]
    print(palindromes)


# Task 20: get list with squares of entered numbers

def the_twentieth():
    print(*[i ** 2 for i in range(5)], sep='\n')


# Task 21: get list with numbers from the string

def the_twenty_first():
    s = '2 4 6'.split()
    num = [i for i in s]
    print(*num, sep='\n')


# Task 22: checking a string for of digits

def the_twenty_second():
    s = 'Number Pi equaled 3.1415'
    print(*[i for i in s if i.isdigit()], sep='')


# Task 23: get quarter of numbers not ending in 4

def the_twenty_third():
    s = '1 2 3 4 5 6 7 8'
    print(*[int(i) ** 2 for i in s.split() if i[-1] in '046'])
