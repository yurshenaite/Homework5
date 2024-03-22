number = int(input('Введите четырехзначное число: '))

a = number // 1000
b = (number % 1000) // 100
c = (number % 100) // 10
d = number % 10

if a == d and b == c:
    print('настоящее')
else:
    print('кривое')