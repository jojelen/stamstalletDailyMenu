#!/usr/bin/env python3
"""
Prints the daily menu of stamstallet in Lund to the console.

Put in .bashrc (and adjust the path):
    alias stamstallet="python3 ~/printStamstalletMenu.py"

@author: Joel Oredsson
"""
from urllib import request, parse
from datetime import date
import re

# Getting todays date
days = ['måndag', 'tisdag', 'onsdag', 'torsdag', 'fredag', 'lördag', 'söndag']
today = days[date.today().weekday()]

tabWidth = 60
print('\n'+'='*tabWidth)
print('Stamställets meny för idag ({})'.format(today).center(tabWidth))
print('='*tabWidth+'\n')

url = 'http://stamstallet.se/lunch/'
try:
    resp = request.urlopen(url).read().decode('utf-8')
except:
    raise SystemExit('[ERROR]: Could not open {}'.format(url))

# removing everything in brakets
bracket = re.compile(r'<.*?>')
text = bracket.sub(r'', resp)

# Get rid of empty spaces
nonEmptyLines = [line.strip()
                 for line in text.split('\n') if line.strip() != '']

# Now, the daily menu is the first "Dagens" and is written in four lines
for i, line in enumerate(nonEmptyLines):
    if line == 'Dagens':
        for n in range(i, i+4):
            print(nonEmptyLines[n].replace('&amp;', '&').center(tabWidth))
        print('\n'+'='*tabWidth+'\n')
        exit()

raise SystemExit('[ERROR]: Could find the daily menu in {}'.format(url))
