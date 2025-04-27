import random

n = 5
lst = [0] * n

def FillList(lst):
    lst = [i + 1 for i in range(n)]
    random.shuffle(lst)
    return lst

def BogoSortList(lst):
    while not is_sorted(lst):
        print(lst)
        random.shuffle(lst)
    return lst

def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:return False
    return True

lst = FillList(lst)
lst = BogoSortList(lst)
print(lst)
