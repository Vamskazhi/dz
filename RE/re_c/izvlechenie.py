#coding: utf-8
import re

def extract_names(filename):
    f = open(filename)
    str = f.read()
    god=re.findall(r'\s(\d+)\</h3>', str)
    god = god.pop(0)

    name=re.findall(r'\<td>(\w*)\</td>', str)
    name1 = ''
    while name:
        name1 = name1 + name.pop(0) + ' '
    name_man=re.findall(r'\d+\s(\w+)', name1)
    name_woman=re.findall(r'\d+\s\w+\s(\w+)', name1)
    ch=re.findall(r'(\d+)\s\w+', name1)
    ch_w = ch[:]
    babynames = []
    babynames.append(god)
    while name_man:
        vs_name_man = name_man.pop(0) + ' ' + ch.pop(0) + ' '
        vs_name_woman = name_woman.pop(0) + ' ' + ch_w.pop(0)
        babynames.append(vs_name_man)
        babynames.append(vs_name_woman)
    babynames.sort()
    #print(babynames)
    return babynames

#extract_names('names/baby1996.html')

