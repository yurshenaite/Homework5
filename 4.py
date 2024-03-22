number = int(input('Введите количество попугаев: '))
number_2 = number % 10

def declension(number_2):
    match number_2:
        case 1:
            declension = 'попугай'
        case 2 | 3 | 4:
            declension = 'попугая'
        case 5 | 6 | 7 | 8 | 9 | 0:
            declension = 'попугаев'
    return declension

result = declension(number_2)
print(number, result)