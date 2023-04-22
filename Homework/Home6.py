# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет
# с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр
# равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется
# написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

n = str(input('Введите номер билета для проверки '))
if len(n) != 6:
    print('Номер билета введен неправильно!')
else:
    i = 0
    sum1 = 0
    sum2 = 0
    while i < 6:
        if i < 3:
            sum1 += int(n[i])
            i += 1
        else:
            sum2 += int (n[i])
            i += 1
    if sum1 == sum2:
        print('Вам повезло, Ваш билет счастливый!')
    else:
        print('В этот раз не повезло')