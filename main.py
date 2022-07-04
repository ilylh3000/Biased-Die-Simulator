#Biased Die

import random


def rolldice(a, b) :
    while True:
        print('Rolling dies...')
        number = random.randint(a, b)
        print(f'You have obtained {number} on die 1')
        break
rolldice(1, 6)

def rolldice1(c, d) :
    while True:
        number1 = random.randint(c, d)
        print(f'You have obtained {number1} on die 2')
        break
rolldice1(5, 6)