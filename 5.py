weight = float(input('Введите вес: '))
height = float(input('Введите рост: '))

weight_kg = weight * 0.454
height_m = height * 0.0254
imt = round((weight_kg / (height_m ** 2)), 2)

if imt < 16:
    print('выраженный дефицит массы тела')
elif 16 <= imt <= 18.49:
    print('недостаточная масса тела')
elif 18.5 <= imt <= 24.99:
    print('норма')
elif 25 <= imt <= 29.99:
    print('избыточная масса тела')
elif 30 <= imt <= 34.99:
    print('ожирение первой степени')
elif 35 <= imt <= 39.99:
    print('ожирение второй степени')
elif imt >= 40:
    print('ожирение третьей степени')