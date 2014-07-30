# preprocess names

f = open('cardlist.txt','r')
ff = f.read().split('\n')
f.close()

import string

# get raw names
rawns = {}
splitns = {}
listns = {}
count = 0
for ii in range(len(ff)-1):
    ss = ff[ii]
    if (ss[0]=='*'):
        sss = ss.replace('-',' ').split(' ')[2:]
        ss2 = ''.join(sss)

