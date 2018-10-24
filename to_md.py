#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 21:39:40 2018
This script is able to use the data from a csv
and transform it to a md table

idea from: https://gist.github.com/samrat/3145260 with mods

@author: booort
"""

# Import libraries

try:
    import csv
except ImportError:
    print('unable to import csv library')

# Define variables (read form archive)
file = open('books_data_csv.csv', 'rt')
books = csv.reader(file)
output_file = open('raw_books.md', 'w')

# Convert from csv to md writing a new archive
for row in books:
    if row[0] == 'title':
        output = "|" + row[0] + "|" + row[1] + "|\n"
        output_file.write(output)
        output = "|---|---|"+"\n"
        output_file.write(output)
    else:
        output = "|**"+row[0]+"**|" + row[1] + "|\n"
        output_file.write(output)
    #print(output)
