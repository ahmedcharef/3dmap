'''
    File name: exportAxes.py
    Author: Ahmed Charef
    Date created: 10/03/2016
    Date last modified: 14/03/2016
    Python Version: 2.7
'''
import mmap
import numpy as np
import re
s = open('posinc02.yaml', "r").read()

x = re.findall(r'x:(.*), ', s)
y = re.findall(r'y:(.*),', s)
z = re.findall(r'z:(.*) ', s)

with open('axeX.txt', 'w') as f: f.write('\n'.join(x))
with open('axeY.txt', 'w') as f: f.write('\n'.join(y))
with open('axeZ.txt', 'w') as f: f.write('\n'.join(z))

print "fine, DONE ;)"
