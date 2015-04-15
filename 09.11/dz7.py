#__author__ = 'vamskazi'
#Напишите программу, которая позволяет пользователю, ввести цитату, выведите цитату  Заглавными,
#строчными буквами, а так же с первой заглавной буквы.
print('enter text')
txt = input()

zagl = txt.upper()
stroch = txt.lower()
pevr_zagl = txt.capitalize()

print(zagl, stroch, pevr_zagl)
