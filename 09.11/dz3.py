#__author__ = 'vamskazi'
#Напишите программу кот. запрашивает у пользователя количество денег в рублях, которые он собирается потратить
#в отпуске, а так же текущий курс евро. Программа должна выводить сумму в евро, без центов.

print('enter sum planned expenditures')
sum  = input()
sum = float(sum)

print('enter euro')
kurs = input()
kurs = float(kurs)

rez = sum / kurs
if (rez < 1):
    print('too small sum')
else:
    rez = round(rez)
    print('your amount =', rez )
