#__author__ = 'vamskazi'
#Напишите программу кот. запрашивает у пользователя радиус и считает длину  и площадь окружности.

#p = r*2П
#S = П*r^2
import math
print('enter radius')
r = input()
r = float(r)
pi = math.pi

P = r * (2 * pi)
S = pi * r ** 2
print('length circle is', P, '\narea of the circle is', S )
