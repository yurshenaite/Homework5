n = int(input('Введите количество кнатов: '))

sikle = 29
galleon = 17 * 29
total_galleon = n // galleon
ost = ((n / galleon) * 100) % 100
total_sikle = int(ost // 29)
knats = int(((ost / 29) * 10))

if total_galleon == 0:
    print(f'{total_sikle} сиклей, {knats} кнатов')
elif ost > 29:
    print(f'{total_galleon} галлеонов, {total_sikle} сиклей, {knats} кнатов')
elif ost == 29:
    print(f'{total_galleon} галлеонов, {total_sikle} сиклей')
elif ost < 29:
    print(f'{total_galleon} галлеонов, {(n - galleon)} кнатов')