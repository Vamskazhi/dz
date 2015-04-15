#__author__ = 'vamskazi'
#Круглый бассейн х метров в диаметре. Сколько литров воды поместиться в бассейне (глубина везде одинакова).
#V=π* r^2* h

import math
pi = math.pi

print('enter the depth of the pool')
depth = input()
depth = float(depth)
print('enter the diameter of the pool')
d = input()
d = float(d)
r = d / 2

V = pi * r ** 2 * depth

print('fit in the pool', V  )