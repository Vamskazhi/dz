#coding: utf-8
import re

def rec1(filename):
    f = open('invoice.txt')
    str = f.read()
    match=re.findall(r'\.*\s\d+\s\d+\W?\d', str)
    print(match)
    summ = 0
    while match:
        punkt = match.pop(0)
        kolvo_cena = punkt.split(' ')
        p1 = kolvo_cena.pop(1)
        kolvo = int(p1)
        p2 = kolvo_cena.pop(1)
        cena = float(p2)
        rez1 = kolvo * cena
        summ += rez1
    print (summ)
    return summ


rec1('invoice.txt')

