number_first=int(input('Введите число: '))
number_second=int(input('Введите число: '))
number_third=int(input('Введите число: '))
if number_first==number_second and number_first==number_third:
    print(3)
elif number_first==number_second or number_first==number_third:
    print(2)
else:
    print(0)