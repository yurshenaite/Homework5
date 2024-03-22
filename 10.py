pincode = input('Придумайте Пин-код: ')

if pincode.isdigit() == True and len(pincode) == 4:
    pincode = int(pincode)
    if pincode < 1900 or pincode > 2050:
        a = pincode // 1000
        b = (pincode % 1000) // 100
        c = (pincode % 100) // 10
        d = pincode % 10
        if a != b and a != c and a != d and b != c and b != d and c != d:
            print('OK')
        else:
            print('ERROR')
    else:
        print('ERROR')
else:
    print('ERROR')