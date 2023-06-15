d={'00':' ','01':' ','02':' ','10':' ','11':' ','12':' ','20':' ','21':' ','22':' '}
def playground (d):

    print (f"  0 1 2")
    print (f"0 {d['00']} {d['01']} {d['02']}")
    print (f"1 {d['10']} {d['11']} {d['12']}")
    print (f"2 {d['20']} {d['21']} {d['22']}")

print ('Добро пожаловать в игру «Крестики-нолики». Правила классические, первый ход за игроком крестика. Ход вводится в формате: координата по оси абсцисс,Enter, координата по оси ординат,Enter ваш ход(х или о, обязательно в русской раскладке...Инициализирую игровое поле:')
playground (d)
while True:
    x,y,n=str(input('Вводите ваши входные данные')),str(input()),str(input())
    v=x+y
    if d[v]!=' ':
        print ('Игровое поле уже занято, ваш ход потрачен')
    else:
        d.update({v: n})
    playground (d)
    if (d['00'] == d['01'] == d['02'] != ' ' or
            d['10'] == d['11'] == d['12'] != ' ' or
            d['20'] == d['21'] == d['22'] != ' ' or
            d['00'] == d['10'] == d['20'] != ' ' or
            d['01'] == d['11'] == d['21'] != ' ' or
            d['02'] == d['12'] == d['22'] != ' ' or
            d['00'] == d['11'] == d['22'] != ' ' or
            d['02'] == d['11'] == d['20'] != ' '):
        print('Игра окончена, поздравляю победителя!')
        break
    elif all(value != ' ' for value in d.values()):
        print ('Ничья!')
        break
