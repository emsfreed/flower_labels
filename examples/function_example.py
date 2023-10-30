import random

def is_even(x):
    return x % 2 == 0

def is_odd(num):
    return num % 2 == 1

def do_i_like_this(task):
    if 'cleaning' in task:
        return False
    else:
        return True

two_is_even = is_even(2)
print(two_is_even)

x = 14
while is_even(x):
    print(x)
    x += random.randint(0,100)