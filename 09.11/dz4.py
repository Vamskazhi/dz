#__author__ = 'vamskazi'
#Улучшите предыдущую программу, что бы она возвращала количество банкнот по 50, 20,10 и 5 Евро
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
    b_50 = round(rez / 50)
    b_20 = round(rez / 20)
    b_10 = round(rez / 10)
    b_5 = round(rez / 5)
    print('your amount =', rez,
          'for this', b_50, 'on 50 bill', 'or', b_20, 'on 20 bill', 'or', b_20, 'on 10 bill', 'or', b_10, 'on 50 bill','or', b_5)
