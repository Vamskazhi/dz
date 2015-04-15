#coding: utf-8
import re

str = '+7-913-432-12-32, +7 (383) 432 1232,  +74213214213'

#match=re.findall(r'\.*\s\d+\s\d+\W?\d', str)

def rec(s):
    match=re.findall(r'\+\d\-*\s*\(*\d\d\d\)*\-*\s*\d\d\d\s*\-*\d\d\-*\d\d', str)
    print(match)

rec(str)