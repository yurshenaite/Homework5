import turtle
import math

xc = float(input('Введите координаты х окружности: '))
yc = float(input('Введите координаты у окружности: '))
r = float(input('Введите радиус окружности: '))
x = float(input('Введите координаты х точки: '))
y = float(input('Введите координаты у точки: '))

turtle.penup()
turtle.goto(xc, yc - r)
turtle.pendown()
turtle.pencolor('black')
turtle.circle(r)
turtle.penup()

turtle.goto(x, y)
turtle.pendown()
turtle.dot(10, 'red')
turtle.penup()

distance = math.sqrt((x - xc)**2 + (y - yc)**2)
if distance < r:
    turtle.goto(-50, -100)
    turtle.pendown()
    turtle.pencolor('red')
    turtle.write('Точка внутри окружности')
elif distance > r:
    turtle.goto(-50, -100)
    turtle.pendown()
    turtle.pencolor('red')
    turtle.write('Точка вне окружности')
else:
    turtle.goto(-50, -100)
    turtle.pendown()
    turtle.pencolor('red')
    turtle.write('Точка на окружности')

turtle.done()