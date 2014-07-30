# preprocess names

f = open('cardlist.txt','r')
ff = f.read().split('\n')
f.close()

import string

# get raw names
rawns = {}
for ii in range(len(ff)-1):
    ss = ff[ii]
    if (ss[0]=='*'):
        sss = ss.split(' ')[2:]
        ss2 = ''.join(sss)
        rawns[ss2]=1
ns = rawns.keys()


o = open('p_cardlist.txt','w')
f.write('\n'.join(ns))
