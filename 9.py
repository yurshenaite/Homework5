high_1, high_2, high_3 = map(int, input('Введите высоты башен: ').split())

big = max(high_1, high_2, high_3)
little = min(high_1, high_2, high_3)
middle = (high_1 + high_2 + high_3) - big - little

print(big, middle, little)