day_1 = int(input('Сколько подданых видели улыбку за первый день?: '))
day_2 = int(input('Сколько подданых видели улыбку за второй день?: '))
day_3 = int(input('Сколько подданых видели улыбку за третий день?: '))

if day_1 == day_2 == day_3:
    print(3)
elif day_1 == day_2 or day_1 == day_3 or day_2 == day_3:
    print(2)
else:
    print(0)