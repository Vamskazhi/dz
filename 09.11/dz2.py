#__author__ = 'vamskazi'
#У холодильника и у лифта есть высота длина и ширина.
#Напишите программу которая считает сколько останется места в лифте если туда поместить холодильник.
# Если холодильник входит в лифт, вывести на экран сколько осталось свободного места в лифте.
# Если холодильник не войдет в лифт, сообщить об этом пользователю.
#elevator height=2500, length=2400, width=2300
#refrigerator height=1856, length=550, width=540,

el_height = 2500
el_length = 2400
el_width = 2300
el_ar = el_length * el_width

print('Enter the height of the refrigerator')
r_h = input()
r_h = int(r_h)
print('Enter the length of the refrigerator')
r_l = input()
r_l = int(r_l)
print('Enter the width of the refrigerator')
r_w = input()
r_w = int(r_w)
r_ar = r_l * r_w
free_area = el_ar - r_ar

if (r_h >= el_height) | (r_ar >= el_ar):
    print('This refrigerator is not for this elevator')

else:
    print ('free area of the elevator', free_area)