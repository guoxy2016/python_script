"""

"""
from decimal import *

notes = map(Decimal, ['100', '50', '20', '10', '5', '1', '0.5', '0.1'])


def change():
    result = '需要'
    give, pay = input('Please input `give_money pay_money`, Use space separation.like "18.50 15"\n').split()
    give, pay = map(Decimal, [give, pay])
    if give < pay:
        print('Don\'t have enough money to pay!')
        return
    money = give - pay
    print(money)
    give_change = {}
    for c in notes:
        num = money // c
        if num != 0:
            give_change[str(c)] = int(num)
        money -= num * c
    for k, v in give_change.items():
        result += '%s元的纸币%s张 ' % (k, v)
    print(result)


while True:
    try:
        change()
    except EOFError:
        break
