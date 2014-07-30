# preprocess names

f = open('cardlist.txt','r')
ff = f.read().split('\n')
f.close()

import string

# get raw names
rawns = {}
listns={}
count=0
for ii in range(len(ff)-1):
    ss = ff[ii]
    if (ss[0]=='*'):
        sss = ss.split(' ')[2:]
        ss2 = ' '.join(sss)
        if (rawns.get(ss2,0)==0):
            rawns[ss2]=count
            listns[count]=ss2
            count=count+1

ns = [listns[k] for k in range(len(rawns.keys()))]


o = open('p_cardlist.txt','w')
o.write('\n'.join(ns))
o.close()
