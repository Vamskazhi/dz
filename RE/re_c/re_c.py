__author__ = 'vamskazi'
#coding: utf-8
import sys
import os
import re
import izvlechenie



def main():
    name_po_str = izvlechenie.extract_names('names/baby1996.html')
    name_po_str_1 = ''
    args = sys.argv[1:]

    if not args:
        print 'usage: [--summaryfile] file [file ]'
        while name_po_str:
            name_po_str_1 = name_po_str.pop()
            print(name_po_str_1)
        sys.exit(1)

        summary = False

    if args[0] == '--summaryfile':
        summary = True
        file = open('1.txt','w')
        name_list = []
        while name_po_str:
            name_po_str_1 = name_po_str.pop(0)
            name_list.append(name_po_str_1)
        print >> file, name_list
        file.close()
        del args[0]

    return 0



if __name__ == '__main__':
    main()

