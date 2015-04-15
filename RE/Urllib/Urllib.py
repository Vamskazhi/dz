#__author__ = 'vamskazi'
# -*- coding: utf-8 -*-
import urllib
import re
#a. Напишите программу – «SuperBrowser».
#В качестве аргумента программе передается url-адрес,
#программа должна сохранить страницу
#по этому адресу в локальный файл в текущей
#директории с соответствующим  именем и расширением html.

ufile = urllib.urlopen('http://yandex.ru')
html = ufile.read()

name = ufile.geturl()
name = name[7:len(name)-1]
#print(name)

name = name + '.html'
file = open(name,'w')

print >> file, html








